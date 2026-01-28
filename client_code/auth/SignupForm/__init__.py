from ._anvil_designer import SignupFormTemplate
from anvil import *
import anvil.server
import anvil.users
import logging

logger = logging.getLogger(__name__)


class SignupForm(SignupFormTemplate):
    """
    M3-compliant signup/registration form.
    
    Purpose:
        New user account creation with business profile setup.
    
    Ready for:
        - M3 component addition in Anvil Designer
        - Event handler implementation
        - Server-side account creation integration
    
    Architecture:
        UI Form → Server Module (server_auth.service)
    """
    
    def __init__(self, **properties):
        """Initialize signup form with M3 configuration."""
        # Initialize components
        self.init_components(**properties)
        
        # Configure M3 components (after Designer work)
        self._configure_m3_components()
    
    def _configure_m3_components(self):
        """
        Configure M3 component roles and properties.
        
        To be implemented after components are added in Designer:
        - Title: Heading with role='headline-large'
        - Subtitle: Text with role='body-medium'
        - Business name field: TextBox with role='outlined'
        - Email field: TextBox with role='outlined', type='email'
        - Password field: TextBox with role='outlined', hide_text=True
        - Confirm password field: TextBox with role='outlined', hide_text=True
        - Create account button: Button with role='filled-button'
        - Sign in link: Button with role='text-button' or NavigationLink
        - Error label: Text with role='body-small', foreground='theme:Error'
        """
        # TODO: Add M3 role configuration after components added in Designer
        # Example:
        # self.lbl_title.role = 'headline-large'
        # self.txt_business_name.role = 'outlined'
        # self.txt_email.role = 'outlined'
        # self.txt_password.role = 'outlined'
        # self.btn_create_account.role = 'filled-button'
        pass
    
    # Event handlers will be added here after Designer work
    # Pattern:
    # def btn_create_account_click(self, **event_args):
    #     """Handle account creation - delegate to server."""
    #     result = anvil.server.call('server_auth.signup', user_data)
    #     if result['success']:
    #         open_form('dashboard.DashboardForm')
    #     else:
    #         self._show_error(result['error'])
