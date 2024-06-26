import anvil.secrets
import anvil.email
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def product_details(product_id, product_name, product_group,product_description, product_categories,processing_fee,  extension_fee, membership_type, interest_type, max_amount, min_amount, min_tenure, max_tenure, roi, foreclose_type, foreclosure_fee, extension_allowed, emi_payment, min_months,lapsed_fee, default_fee, npa ,occupation,min_extension_month):
  row = app_tables.fin_product_details.add_row(product_id=product_id,
                                           product_name = product_name,
                                           product_group=product_group,
                                           product_description = product_description,
                                           product_categories = product_categories,
                                           processing_fee=processing_fee,   
                                           extension_fee=extension_fee,
                                           membership_type=membership_type,
                                           interest_type= interest_type,
                                           # late_fee = late_fee,
                                           max_amount = max_amount,
                                           min_amount=min_amount,
                                           # tenure = tenure,
                                           min_tenure = min_tenure,
                                           max_tenure = max_tenure,
                                           roi = roi,
                                           foreclose_type=foreclose_type,
                                           foreclosure_fee = foreclosure_fee,
                                           extension_allowed=extension_allowed,
                                           # lapsed_status=lapsed_status,
                                           emi_payment = emi_payment,
                                           min_months=min_months,                                           
                                           #discount_coupons = discount_coupons,
                                           lapsed_fee = lapsed_fee,
                                           default_fee = default_fee,
                                           npa=npa,
                                           occupation=occupation,
                                           min_extension_months=min_extension_month
                                          )



@anvil.server.callable
def manage_products(groups,category):
  row = app_tables.fin_product_categories.add_row(product_group=groups,product_category=category)


@anvil.server.callable
def user_issues_bugreports(user_issues, specific_issue, user_discription, image, feedback_form, email_user,coustmer_id):
 row = app_tables.fin_user_issues_bugreports.add_row(user_issues=user_issues,
                                                 user_discription=user_discription,
                                                 specific_issue=specific_issue,
                                                 image=image,
                                                 feedback_form=feedback_form,
                                                 email_user=email_user,
                                                 customer_id=coustmer_id)

# code for basic details
@anvil.server.callable
def add_basic_details(full_name, gender, dob, mobile_no, user_photo, alternate_email, aadhar, aadhar_card, pan, pan_card, street_adress_1, street_address_2, city, pincode, state, country, user_id, user_age ,present, duration):
  row = app_tables.fin_user_profile.search(customer_id=user_id)
  if row:
    row[0]['full_name'] = full_name
    row[0]['gender'] = gender
    row[0]['date_of_birth'] = dob
    row[0]['mobile']=mobile_no
    row[0]['user_photo']=user_photo
    row[0]['another_email']= alternate_email
    row[0]['aadhaar_no']=aadhar
    row[0]['aadhaar_photo']=aadhar_card
    row[0]['pan_number']=pan
    row[0]['pan_photo']=pan_card
    row[0]['street_adress_1'] = street_adress_1
    row[0]['street_address_2'] = street_address_2
    row[0]['city'] = city
    row[0]['state'] = state
    row[0]['country'] = country
    row[0]['pincode'] = pincode
    row[0]['user_age'] = user_age
    row[0]['present_address'] = present
    row[0]['duration_at_address'] = duration
    # row[0]['form_count'] = 0

@anvil.server.callable
def generate_admin_id():
    full_table = app_tables.fin_user_profile.search()
    if full_table:
        highest_customer_id = find_highest_customer_id()
        return highest_customer_id + 1
    else:
        return 100000

def find_highest_customer_id():
    table_data = app_tables.fin_user_profile.search()
    highest_id = 99999
    for row in table_data:
        customer_id = row['customer_id']
        if customer_id > highest_id:
            highest_id = customer_id
    return highest_id



import bcrypt

@anvil.server.callable
def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()

# for view admins
@anvil.server.callable
def get_admin_emails():
    # Fetch all admin emails from the fin_admin_users table
    admin_emails = [admin['admin_email'] for admin in app_tables.fin_admin_users.search()]
    return admin_emails

@anvil.server.callable
def get_admin_details(email):
    # Fetch admin details based on email from the fin_admin_users table
    admin = app_tables.fin_admin_users.get(admin_email=email)
    if admin:
        admin_details = {
            'admin_email': admin['admin_email'],
            'full_name': admin['full_name'],
            'admin_role':admin['admin_role'],
            'ref_admin_name':admin['ref_admin_name'],
            'joined_date':admin['join_date']
        }
        return admin_details
    else:
        return None

