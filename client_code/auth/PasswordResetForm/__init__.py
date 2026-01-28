from ._anvil_designer import PasswordResetFormTemplate
from anvil import *
import anvil.server
import anvil.users
import logging

logger = logging.getLogger(__name__)


class PasswordResetForm(PasswordResetFormTemplate):
    """
    M3-compliant password reset form.
    
    Purpose:
        User password reset request and confirmation.
    
    Ready for:
        - M3 component addition in Anvil Designer
        - Event handler implementation
        - Server-side password reset integration
    
    Architecture:
        UI Form → Server Module (server_auth.service)
    """
    
    def __init__(self, **properties):
        """Initialize password reset form with M3 configuration."""
        # Initialize components
        self.init_components(**properties)
        
        # Configure M3 components (after Designer work)
        self._configure_m3_components()
    
    def _configure_m3_components(self):
        """
        Configure M3 component roles and properties.
        
        To be implemented after components are added in Designer:
        - Title: Heading with role='headline-large'
        - Instructions: Text with role='body-medium'
        - Email field: TextBox with role='outlined', type='email'
        - Reset button: Button with role='filled-button'
        - Back to login link: Button with role='text-button' or NavigationLink
        - Success/Error messages: Text with role='body-small'
        """
        # TODO: Add M3 role configuration after components added in Designer
        # Example:
        # self.lbl_title.role = 'headline-large'
        # self.txt_email.role = 'outlined'
        # self.btn_reset.role = 'filled-button'
        pass
    
    # Event handlers will be added here after Designer work
    # Pattern:
    # def btn_reset_click(self, **event_args):
    #     """Handle password reset request - delegate to server."""
    #     result = anvil.server.call('server_auth.request_password_reset', email)
    #     if result['success']:
    #         self._show_success("Password reset email sent!")
    #     else:
    #         self._show_error(result['error'])
