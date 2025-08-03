#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_api_project.settings')
    
    # Add this line BEFORE any django setup
    os.environ.setdefault('DJ_REST_AUTH_TOKEN_MODEL', 'None')

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



if __name__ == '__main__':
    main()
