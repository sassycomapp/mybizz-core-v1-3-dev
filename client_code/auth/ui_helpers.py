import anvil.server
"""
Auth UI Helper Functions

Pure display/formatting functions for auth-related UI operations.
All business logic and validation moved to server_code/server_auth/.

M3-compliant utilities for displaying user information.
"""

from typing import Optional


def format_user_display_name(user: Optional[dict]) -> str:
    """
    Format user's display name from user row.
    
    Args:
        user: User row from users table
        
    Returns:
        Formatted display name (e.g., "John Doe", "John", or email username)
        
    Example:
        >>> format_user_display_name({'first_name': 'John', 'last_name': 'Doe'})
        'John Doe'
    """
    if not user:
        return "Guest"

    first_name = user.get('first_name', '')
    last_name = user.get('last_name', '')

    if first_name and last_name:
        return f"{first_name} {last_name}"
    elif first_name:
        return first_name
    elif last_name:
        return last_name
    else:
        # Fallback to email username
        email = user.get('email', '')
        return email.split('@')[0] if email else "User"


def get_user_initials(user: Optional[dict]) -> str:
    """
    Get user initials for avatar display.
    
    Args:
        user: User row
        
    Returns:
        User initials (max 2 characters uppercase)
        
    Example:
        >>> get_user_initials({'first_name': 'John', 'last_name': 'Doe'})
        'JD'
    """
    if not user:
        return "?"

    first_name = user.get('first_name', '')
    last_name = user.get('last_name', '')
    email = user.get('email', '')

    if first_name and last_name:
        return f"{first_name[0]}{last_name[0]}".upper()
    elif first_name:
        return first_name[0:2].upper()
    elif email:
        return email[0:2].upper()
    else:
        return "U"


def format_role_display(role: str) -> str:
    """
    Format user role for display with emoji.
    
    Args:
        role: User role ('owner', 'manager', 'staff', 'customer')
        
    Returns:
        Formatted role with emoji (e.g., '👑 Owner')
        
    Example:
        >>> format_role_display('owner')
        '👑 Owner'
    """
    role_map = {
        'owner': '👑 Owner',
        'manager': '⭐ Manager',
        'staff': '👤 Staff',
        'customer': '🛍️ Customer',
        'admin': '🔑 Admin'
    }

    return role_map.get(role, role.title())


def format_last_login(last_login_time) -> str:
    """
    Format last login time for display.
    
    Args:
        last_login_time: Last login timestamp (datetime)
        
    Returns:
        Formatted time string (e.g., '2 hours ago', 'Just now')
        
    Example:
        >>> format_last_login(datetime.now() - timedelta(hours=2))
        '2 hours ago'
    """
    if not last_login_time:
        return "Never"

    from datetime import datetime, timedelta

    now = datetime.now()
    diff = now - last_login_time

    if diff.days > 365:
        years = diff.days // 365
        return f"{years} year{'s' if years > 1 else ''} ago"
    elif diff.days > 30:
        months = diff.days // 30
        return f"{months} month{'s' if months > 1 else ''} ago"
    elif diff.days > 0:
        return f"{diff.days} day{'s' if diff.days > 1 else ''} ago"
    elif diff.seconds > 3600:
        hours = diff.seconds // 3600
        return f"{hours} hour{'s' if hours > 1 else ''} ago"
    elif diff.seconds > 60:
        minutes = diff.seconds // 60
        return f"{minutes} minute{'s' if minutes > 1 else ''} ago"
    else:
        return "Just now"


def format_account_status(status: str) -> str:
    """
    Format account status for display with indicator.
    
    Args:
        status: Account status ('active', 'inactive', 'suspended', 'pending')
        
    Returns:
        Formatted status with indicator emoji
        
    Example:
        >>> format_account_status('active')
        '✅ Active'
    """
    status_map = {
        'active': '✅ Active',
        'inactive': '⏸ Inactive',
        'suspended': '🚫 Suspended',
        'pending': '⏳ Pending Verification'
    }

    return status_map.get(status, status.title())


# Export all helper functions
__all__ = [
    'format_user_display_name',
    'get_user_initials',
    'format_role_display',
    'format_last_login',
    'format_account_status'
]
