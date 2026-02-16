#!/bin/bash

# Configuration: Define your two destination URLs
DEST_A="gand0rf@http://192.168.50.81:3000/gand0rf/sys_scan.git"
DEST_B="gand0rf@http://192.168.50.81:3000/gand0rf/sys_scan.git"

# Get current origin URL
CURRENT_URL=$(git remote get-url origin)

if [ "$CURRENT_URL" == "$DEST_A" ]; then
    echo "Switching from A to B..."
    git remote set-url origin "$DEST_B"
else
    echo "Switching from B to A (or other to A)..."
    git remote set-url origin "$DEST_A"
fi

# Verify the change
echo "New remote origin is:"
git remote -v