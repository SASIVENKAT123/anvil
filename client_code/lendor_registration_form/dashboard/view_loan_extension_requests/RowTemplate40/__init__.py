from ._anvil_designer import RowTemplate40Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class RowTemplate40(RowTemplate40Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.   

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    selected_row = self.item
    print(f"Selected row status: {selected_row['status']}")
    open_form("lendor_registration_form.dashboard.view_loan_extension_requests.extension_details", selected_row=selected_row)
    if selected_row['status'] == 'approved' or selected_row['status'] == 'rejected':
        open_form("lendor_registration_form.dashboard.view_loan_extension_requests.extension_details_approved_or_rejected", selected_row=selected_row)
    else:
        # open_form("lendor_registration_form.dashboard.vlfr.foreclose_details")
       None
