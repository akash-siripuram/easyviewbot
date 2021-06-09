import streamlit as st
import sqlite3
import pandas as pd

con=sqlite3.connect("bismillah.db")
c=con.cursor()



def create_usertable():
	c.execute("CREATE TABLE IF NOT EXISTS user_table3(id integer primary key autoincrement, instalink Text NOT NULL,plan text NOT NULL,ph_no text NOT NULL,status text)")
	

def add_userdata(instalink,plan,ph_no,stats):
	c.execute("INSERT INTO user_table3(instalink,plan,ph_no,status) VALUES(?,?,?,?)",(instalink,plan,ph_no,stats))
	con.commit()

def view_link_plan():
	c.execute("Select instalink as Instagram_Link,plan as Selected_Plan from user_table3")
	data=c.fetchall()
	return data
def view_plan_phno():
	c.execute("Select plan as Selected_Plan,ph_no as Phone_Number from user_table3")
	data=c.fetchall()
	return data
def view_phno_link():
	c.execute("Select instalink as Instagram_Link,ph_no as Phone_Number from user_table3")
	data=c.fetchall()
	return data
def delete_table():
	c.execute("DROP TABLE user_table3")
	
def view_instalink():
	c.execute("Select id,instalink,status from user_table3")
	data=c.fetchall()
	return data
def view_plan():
	c.execute("Select id,plan,status from user_table3")
	data=c.fetchall()
	return data
def change_status(status,row_id):
	c.execute("update user_table3 set status=? where id =?",(status,row_id))
	con.commit()
def give_id(plan,ph_no):
	c.execute("SELECT id FROM user_table3 where plan = ? and ph_no = ? ORDER BY id DESC LIMIT 3",(plan,ph_no))
	data=c.fetchall()
	return data
def view_status(row_idd):
	c.execute("Select status from user_table3 where id=?",(row_idd,))
	data=c.fetchall()
	return data




#----------------------------------------



def insta_link(a,b,c):

	if c ==1 :
		st.subheader("4. Enter your Instagram ID")
		link="a"
		if st.checkbox("How to find my Instagram ID?"):
			st.info("""
			Follow these steps regarding how to select ID
			
	        To get a link to a post in Android and ios:
	                 1.Go to Profile.
	                 2.Select Instagram Id on top of Edit Profie option.
	        To get a link to a post from the web:
	                 1.Go to Profile.
	                 2.Select Instagram Id which is on Left side of Edit Profie option.
			""")	
		link=st.text_input("Copy and paste the ID below","")
		st.info("Make sure your ID is correct and exact")
		st.success("We are paying for you, So it is free. Please share it with your friends")	
		st.subheader("")
		if st.button("Click here, We paid for you"):
			if len(link) > 0 and len(b) ==10:
				create_usertable()
				add_userdata(link,a,b,"Processing")
				st.write("You have completed it in just 4 Steps")
				payout="""
				<div style="background-color:#DD2A7B;padding:0px">
				<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Payment</h2>
				</div>
				"""
				st.markdown(payout,unsafe_allow_html=True)
				st.warning("Your chosen plan is {}".format(a))
				st.success("We are paying for you, So it is free. Please share it with your friends")
				lis=give_id(a,b)
				tup=lis[0]
				st.write("You can track your order status with this id -> ",tup[0])
				st.subheader("")
				st.warning("Your Request will be processed in less than 1 hr after your payment")
				#st.warning("")
			else:
				st.warning("Fields are missing")


	elif c==0:
		
		st.subheader("4. Enter your Instagram Post link")
		if st.checkbox("How to find my Instagram Link?"):
			st.info("""
			Follow these steps regarding how to select link	
			
	        To get a link to a post in Android and ios:
	                 1.Tap ...(Three dots) above the post.
	                 2.Tap Copy Link.
	        To get a link to a post from the web:
	                 1.Open your web browser.
	                 2.Go to instagram.com/username. For example, if the username is "johnsmith," type in instagram.com/johnsmith as the URL.
	                 3.Click the post you want to save and copy the link at the top of your browser.
			""")
		link="a"	
		link=st.text_input("")
		st.info("Make sure your link is correct")
		#st.subheader("")
		#st.subheader("")
		#st.success(" -  9493736321@okbizaxis  ".format(a))
		st.subheader("")
		if st.button("Click Here to submit"):
			if len(link) > 0 and len(b) ==10:
				create_usertable()
				add_userdata(link,a,b,"Processing")
				st.write("You have completed it in just 4 Steps")
				payout="""
				<div style="background-color:#DD2A7B;padding:0px">
				<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Payment</h2>
				</div>
				"""
				st.markdown(payout,unsafe_allow_html=True)
				st.warning("Your chosen plan is {}".format(a))
				st.success("""

			    Send money using Google pay, Phone Pe, Paytm to this Number with Order ID(Mentioned below) as remarks	
			
	            9493736321

			    """)
				lis=give_id(a,b)
				tup=lis[0]
				st.write("You can track your order status with this id -> ",tup[0])
				st.subheader("")
				st.warning("Your Request will be processed in less than 1 hr after your paymemt")
				#st.warning("Your Request will be processed in less than 1 hr")
			else:
				st.warning("Fields are missing")
	else:
		
		st.subheader("4. Enter your Instagram ID")
		link="a"
		if st.checkbox("How to find my Instagram ID?"):
			st.info("""
			Follow these steps regarding how to select ID
			
	        To get Instagram ID in Android and ios:
	                 1.Go to Profile.
	                 2.Select Instagram Id on top of Edit Profie option.
	        To get Instagram ID from the web:
	                 1.Go to Profile.
	                 2.Select Instagram Id which is on Left side of Edit Profie option.
			""")	
		link=st.text_input("Copy and paste the ID below","")
		st.info("Make sure your ID is correct and exact")
		#st.subheader("")
		st.subheader("")
		if st.button("Click here and send the money"):
			if len(link) > 0 and len(b) ==10:
				create_usertable()
				add_userdata(link,a,b,"Processing")
				st.write("You have completed it in just 4 Steps")
				payout="""
				<div style="background-color:#DD2A7B;padding:0px">
				<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Payment</h2>
				</div>
				"""
				st.markdown(payout,unsafe_allow_html=True)
				st.warning("Your chosen plan is {}".format(a))
				st.success("""

			    Send money using Google pay, Phone Pe, Paytm to this Number with Order ID(Mentioned below) as remarks/message	
			
	            9493736321

			    """)
				lis=give_id(a,b)
				tup=lis[0]
				st.write("You can track your order status with this id -> ",tup[0])
				st.subheader("")
				st.warning("Your Request will be processed in less than 1 hr after your payment")
				#st.warning("Your Request will be processed in less than 1 hr")
			else:
				st.warning("Fields are missing")			

def admin():
	st.write("You are in admin page now")
	st.warning("This page is for Admin")
	st.info("If you are user, please select Normal user option to use this website")
	a=st.text_input("Username","admin")
	b=st.text_input("Password","",type="password")
	if a == "admin" and (b=="insta" or b == "Insta"):
		st.success("You logged in as admin")
		st.subheader("What do you want to view")
		s=st.selectbox("",["Plan and Phone number","Instagram Link and Plan","Instagram Link and Phone Number","Instagram Link","Plan"])
		if s == "Plan and Phone number":
			data=view_plan_phno()
			df=pd.DataFrame(data)
			df_new = df.rename(columns={'0': 'Selected_Plan','1':'Phone_Number'})
			st.dataframe(df_new)

		elif s == "Instagram Link and Plan":
			data=view_link_plan()
			st.dataframe(data)
		elif s== "Instagram Link and Phone Number":
			data=view_phno_link()
			st.dataframe(data)
		elif s== "Instagram Link":
			data=view_instalink()
			st.dataframe(data)
		elif s== "Plan":
			data=view_plan()
			st.dataframe(data)
		if st.button("Delete All Rows"):
			delete_table()	
		st.subheader("Dear, Admin Update enter user id and click success after transaction")
		row_id=st.text_input("Enter the ID you have completed(Exactly)")
		if st.button("Success"):
			change_status("Success",row_id)

			
		st.subheader("Dear, Admin These are the Links to the Plans")	
		plann=st.selectbox("",("Views","No_Refill-Followers","Refill-Followers","Likes","Free_Followers"))
		if plann == "Views":
			st.write("https://socialdaddy.in/default.aspx?cat=55")
			st.write("Select this -> 1.Insagram Views 2.Instagram Likes [15k] [Working After Update]- 57 INR")
		elif plann == "No_Refill-Followers":
			st.write("https://socialdaddy.in/default.aspx?cat=55")
			st.write("Select this -> 1.Instagram Followers(No-Refill) 2.Instagram Followers Real Mixed [15k]- 130 INR")
			
		elif plann == "Refill-Followers":
			st.write("https://socialdaddy.in/default.aspx?cat=55")
			st.write("Select this -> 1.Instagram Followers(Refill) 2.Instagram Followers [Refill 45 Days] [New]- 156 INR")
			
		elif plann == "Likes":
			st.write("https://socialdaddy.in/default.aspx?cat=55")
			st.write("Select this -> 1.Instagram Likes 2.Instagram Likes [15k] [Working After Update]- 57 INR")
			
		elif plann == "Free_Followers":
			st.write("https://famoid.com/get-free-instagram-followers/")
			st.write("https://temp-mail.org/en/")
			
				

def normal_user():
	head="""
		<div style="background-color:#515BD4;padding:0px">
		<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Easy-ViewBot</h2>		
		</div>
		"""
	st.markdown(head,unsafe_allow_html=True)

	title="""
		<div style="background-color:#DD2A7B;padding:0px">
		<h4 style="color:#ffffff;text-align:center;font-weight:bold;">Do you need Views, followers, likes on instagram ?</h4>
		<h4 style="color:#ffffff;text-align:center;font-weight:bold;">We are here to help you</h4>
		<h4 style="color:#ffffff;text-align:center;font-weight:bold;">Increase your social influence in just 4 Steps</h4>
		</div>
		"""
	st.markdown(title,unsafe_allow_html=True)	
	st.subheader("")
	st.subheader("1. What do you want to increase")
	st.info("** Please make your account PUBLIC for sometime if it is PRIVATE")
	var_a=st.radio("",["Views","Followers","Likes","Free Followers"])
	v_dic={1:"100 Views - 4 INR",2:"1000 Views - 5 INR",3:"10000 Views - 15 INR",4:"100000 Views - 150 INR"}
	if var_a == "Views":
		st.info("** Views are only for videos, If no videos exist in your account select other options(Likes, Followers)")

		st.subheader("2. Select the plan")
		
		v_plan=st.radio("",["100 Views - 4 INR","1000 Views - 9 INR","10000 Views - 29 INR [Recommended]","100000 Views - 49 INR"])
		#st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("+91-")
		if len(ph_no) == 10:
			st.write("")
		else:
			st.warning("Enter correct phone number")

		buff=insta_link(v_plan,ph_no,0)
					    
	elif var_a == "Followers":
		v_plan=""
		st.subheader("2. Select the plan")
		p=st.radio("",["No Refill - Followers will not be added if decreased","Refill - Followers will be added again if decreased in next 45 days"])
		if p == "No Refill - Followers will not be added if decreased":
			v_plan=st.radio("",["50 Followers - 9 INR","100 Followers - 16 INR","200 Followers - 32 INR","400 Followers - 49 INR","500 Followers - 63 INR ","1,000 Followers - 103 INR [Recommended]"])
		elif p == "Refill - Followers will be added again if decreased in next 45 days":
			v_plan=st.radio("",["50 Followers - 13 INR","100 Followers - 24 INR","200 Followers - 44 INR","300 Followers - 66 INR","500 Followers - 99 INR [Recommended]","1000 Followers - 180 INR"])
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("+91-")
		if len(ph_no) == 10:
			st.write("")
		else:
			st.warning("Enter correct phone number")

		buff=insta_link(v_plan,ph_no,9)			 
		#st.warning("{} is selected".format(v_plan))
	elif var_a == "Likes":
		st.subheader("2. Select the plan")
		
		v_plan=st.radio("",["100 Likes - 10 INR","200 Likes - 18 INR","300 Likes - 29 INR","400 Likes - 39 INR","500 Likes - 49 INR [Recommended]","1000 Likes - 98 INR"])
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("+91-")
		if len(ph_no) == 10:
			st.write("")
		else:
			st.warning("Enter correct phone number")

		buff=insta_link(v_plan,ph_no,0)
					
					
	else:
		st.subheader("2. You will get free Followers.")
		st.info("We are paying for you. So, that you trust, use and share our website")
		
		v_plan="25 Free Followers"
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("+91-")
		if len(ph_no) == 10:
			st.write("")
		else:
			st.warning("Enter correct phone number")

		buff=insta_link(v_plan,ph_no,1)
	st.subheader(" ")				
	#st.subheader("Track your order")
	#st.write("")

	track="""
		<div style="background-color:#DD2A7B;padding:0px">
		<h2 style="color:#ffffff;text-align:center;font-weight:bold;">Track your Order</h2>
		</div>
		"""
	st.markdown(track,unsafe_allow_html=True)

	row_idd=st.text_input("Enter your Tracking ID")
	#st.write("This is track id given by user ",row_idd)
	
	if st.button("Track my order"):
		try:
			v_s=view_status(row_idd)
			b=v_s[0]
			if b[0] == "Success":
				st.success("Your order is Successful")
			else:
				st.info("Don't Worry, your order is under process. We will let you know when it is finished")
		except:
			st.warning("Please enter correct order ID")	


			




	st.subheader(" ")
	st.subheader(" ")
	st.subheader(" ")
	st.write("Contact us  -  easy-viewbot@protonmail.com")
		#st.warning("{} is selected".format(v_plan))	

def main():
	
	admin_status=st.radio("",["Normal User","Admin"])
	#st.write(admin_status)
	if admin_status == "Normal User":
		#m,j,k=normal_user()
		normal_user()
		#if len(m)>6:
			#st.write("{}, {}, {}".format(m,j,k))
			
			#st.subheader("")
	else:
		create_usertable()
		admin()

if __name__ == '__main__':
    main()
