#!/usr/bin/env python3

import sys, json, urllib.request

def main():
    events = fetch_events(sys.argv[1])
    display_events(events, sys.argv[2])


def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data
    except Exception as e:
        print(f"Error: {e}")
        return []

def display_events(events, event_type):
    type_mapping = {
        'push': 'PushEvent',
        'issue': 'IssuesEvent', 
        'star': 'WatchEvent',
        'fork': 'ForkEvent'
    }
    
    target_type = type_mapping.get(event_type)
    
    for event in events:
        if event['type'] == target_type:
            repo = event['repo']['name']
            
            if target_type == 'PushEvent':
                commits = len(event['payload']['commits'])
                print(f"User pushed {commits} commits to {repo}")
            elif target_type == 'IssuesEvent':
                action = event['payload']['action']
                print(f"User {action} an issue in {repo}")
            elif target_type == 'WatchEvent':
                print(f"User starred {repo}")
            elif target_type == 'ForkEvent':
                print(f"User forked {repo}")

main()
