# Module for searching the /home directory.
#
# This will look inside directories in /home
# and see if it can find any files named
# user.txt or flag.txt. It will then look
# for a .ssh folder and attempt to see if there
# are any files in it.

import os
import stat

class search:
    def __init__(self):
        pass

    def search_home_directory(self):
        """
        Search /home directory for user.txt/flag.txt files and .ssh folders.
        Returns a dictionary with findings.
        """
        results = {
            'flags': {},
            'ssh_folders': {}
        }
        
        home_dir = '/home'
        
        # Check if /home exists and is accessible
        if not os.path.exists(home_dir):
            return f"Directory {home_dir} does not exist"
        
        if not os.access(home_dir, os.R_OK):
            return f"No read access to {home_dir}"
        
        try:
            # Iterate through user directories in /home
            for user_folder in os.listdir(home_dir):
                user_path = os.path.join(home_dir, user_folder)
                
                # Skip if not a directory
                if not os.path.isdir(user_path):
                    continue
                
                # Search for flag files
                flag_search = self.search_for_flags(user_path, results)
                
                # Search for .ssh folder
                ssh_search = self.search_for_ssh(user_path, user_folder, results)
        
        except PermissionError as e:
            return f"Permission denied accessing {home_dir}: {e}"
        except Exception as e:
            return f"Error scanning {home_dir}: {e}"
        
        return (flag_search, ssh_search)

    def search_for_flags(self,base_path, results):
        """
        Recursively search for user.txt and flag.txt files.
        """
        target_files = ['user.txt', 'flag.txt']
        
        try:
            for root, dirs, files in os.walk(base_path):
                for filename in files:
                    if filename in target_files:
                        file_path = os.path.join(root, filename)
                        
                        # Try to read the file
                        try:
                            with open(file_path, 'r') as f:
                                contents = f.read()
                            results['flags'][filename] = (file_path, contents)
                            return results
                        except PermissionError:
                            results['flags'][filename] = (file_path, "Permission denied")
                            return results
                        except Exception as e:
                            results['flags'][filename] = (file_path, f"Error reading: {e}")
                            return results
        
        except PermissionError:
            pass  # Skip directories we can't access
        except Exception as e:
            return f'Error when searching for flag:\n\n{e}'

    def search_for_ssh(self,user_path, user_folder, results):
        """
        Search for .ssh folder and check accessibility.
        """
        ssh_path = os.path.join(user_path, '.ssh')
        
        if os.path.exists(ssh_path) and os.path.isdir(ssh_path):
            ssh_info = {
                'path': ssh_path,
                'files': []
            }
            
            # Check if we can access the .ssh folder
            if os.access(ssh_path, os.R_OK):
                
                try:
                    # List files in .ssh folder
                    ssh_files = os.listdir(ssh_path)
                    ssh_info['files'] = ssh_files
                    results['ssh_folders'][user_folder] = ssh_info
                except PermissionError:
                    return f"Error: Found .ssh folder but cannot list contents: {ssh_path}"
                except Exception as e:
                    return f'Error: Error with .ssh scan:\n{e}'
            else:
                return f"Error: Found .ssh folder but no access: {ssh_path}"

    def main_entry(self):
        findings = self.search_home_directory()

        if len(findings[0]['flags']) == 0:
            flag_results = '\nFlags found: 0'
        else:
            if 'Error' not in findings[0]['flags']:
                flag_results = f'\nFlags found: {len(findings[0]['flags'])}'
                for flag in findings[0]['flags']:
                    flag_results += (f'\nName: {flag}' + f'\nPath: {findings[0]['flags'][flag][0]}' + f'\nFlag: {findings[0]['flags'][flag][1]}')
            else:
                flag_results = f"\nFlag scan error:\n\n{findings[0]['flags']}"

        if len(findings[0]['ssh_folders']) == 0:
            ssh_result = '\nSSH info found: 0'
        else:
            if 'Error' not in findings[0]['ssh_folders']:
                ssh_result = f'\n\nSSH info found: {len(findings[0]['ssh_folders'])}'
                for ssh in findings[0]['ssh_folders']:
                    ssh_result += f'\nName: {ssh}' + f'\nPath: {findings[0]['ssh_folders'][ssh]['path']}' + f'\nFiles: {findings[0]['ssh_folders'][ssh]['files']}'
            else:
                ssh_result = f"\nssh scan error:\n\n{findings[0]['ssh_folders']}"

        return flag_results + ssh_result

if __name__ == "__main__":
    pass   
