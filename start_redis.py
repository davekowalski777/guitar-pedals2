import redis
import subprocess
import sys
import os
import time

def check_redis():
    try:
        r = redis.Redis(host='localhost', port=6379, db=0)
        r.ping()
        print("Redis is running!")
        return True
    except redis.ConnectionError:
        return False

def main():
    if check_redis():
        print("Redis is already running.")
        return

    print("Starting Redis server...")
    
    # Try different methods to start Redis
    try:
        # Method 1: Using brew services
        subprocess.run(['brew', 'services', 'start', 'redis'])
    except FileNotFoundError:
        try:
            # Method 2: Using redis-server directly
            subprocess.Popen(['redis-server'], 
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
        except FileNotFoundError:
            print("Could not start Redis server. Please install Redis first.")
            sys.exit(1)

    # Wait for Redis to start
    retries = 5
    while retries > 0:
        if check_redis():
            print("Redis server started successfully!")
            break
        print(f"Waiting for Redis to start... ({retries} attempts left)")
        time.sleep(1)
        retries -= 1
    else:
        print("Failed to start Redis server.")
        sys.exit(1)

if __name__ == "__main__":
    main()
