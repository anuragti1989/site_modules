#!/bin/bash

# Configuration settings
APP_DIR="/root/my-web-app"
APP_NAME="web-app"
TUNNEL_NAME="cf-tunnel"
LOCAL_PORT=3000

show_menu() {
    echo "=========================================="
    echo "      PRoot Ubuntu Server Manager         "
    echo "=========================================="
    echo "1) Check Status (PM2 List)"
    echo "2) Live Process Monitor (pm2 monit)"
    echo "3) View All Logs"
    echo "4) View Web App Logs"
    echo "5) View Cloudflare Tunnel Logs"
    echo "6) Test Local App Health (curl)"
    echo "7) Restart All Processes"
    echo "8) Save Current PM2 State"
    echo "9) Exit"
    echo "=========================================="
}

read_option() {
    local choice
    read -p "Enter choice [1-9]: " choice
    case $choice in
        1)
            pm2 list
            ;;
        2)
            pm2 monit
            ;;
        3)
            pm2 logs --lines 50
            ;;
        4)
            pm2 logs "$APP_NAME" --lines 50
            ;;
        5)
            pm2 logs "$TUNNEL_NAME" --lines 50
            ;;
        6)
            echo "Testing http://localhost:$LOCAL_PORT..."
            curl -I "http://localhost:$LOCAL_PORT"
            ;;
        7)
            echo "Restarting services..."
            pm2 restart all
            ;;
        8)
            echo "Saving current PM2 state..."
            pm2 save
            ;;
        9)
            exit 0
            ;;
        *)
            echo "Invalid option."
            ;;
    esac
}

# Run directly with argument or launch interactive menu
if [ -n "$1" ]; then
    case $1 in
        status)  pm2 list ;;
        logs)    pm2 logs --lines 50 ;;
        restart) pm2 restart all ;;
        save)    pm2 save ;;
        test)    curl -I "http://localhost:$LOCAL_PORT" ;;
        *)       echo "Usage: ./manage.sh [status|logs|restart|save|test]" ;;
    esac
else
    while true; do
        show_menu
        read_option
        echo ""
    done
fi
