import streamlit as st
import sqlite3
import pandas as pd

con=sqlite3.connect("bismillah.db")
c=con.cursor()



def create_usertable():
	c.execute("CREATE TABLE IF NOT EXISTS user_table2(instalink Text NOT NULL,plan text NOT NULL,ph_no text NOT NULL)")
	

def add_userdata(instalink,plan,ph_no):
	c.execute("INSERT INTO user_table2(instalink,plan,ph_no) VALUES(?,?,?)",(instalink,plan,ph_no))
	con.commit()

def view_link_plan():
	c.execute("Select instalink as Instagram_Link,plan as Selected_Plan from user_table2")
	data=c.fetchall()
	return data
def view_plan_phno():
	c.execute("Select plan as Selected_Plan,ph_no as Phone_Number from user_table2")
	data=c.fetchall()
	return data
def view_phno_link():
	c.execute("Select instalink as Instagram_Link,ph_no as Phone_Number from user_table2")
	data=c.fetchall()
	return data
def delete_table():
	c.execute("DROP TABLE user_table2")
	
def view_instalink():
	c.execute("Select instalink from user_table2")
	data=c.fetchall()
	return data
def view_plan():
	c.execute("Select plan from user_table2")
	data=c.fetchall()
	return data

#----------------------------------------



def insta_link(a,b):

	
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
	link=st.text_input("Enter the link in the box","https://www.instagram.com/")
	st.warning("Make sure your link is correct")
	st.subheader("")
	st.info("Your chosen plan is {}".format(a))
	st.subheader("")
	if a != "100 Free Views":

	    st.info("Send Money to this below UPI Id")
	    st.success("9493736321@okbizaxis")
	    st.subheader("")
	    if st.button("Click here after Payment"):
		create_usertable()
		add_userdata(link,a,b)
		st.warning("Thank you, We will check your transaction and process your request")
		st.warning("Your Request will be processed in less than 1 hr")
	else:
		st.success("We are paying for you, So it is free. Please share it with your friends")	
		st.subheader("")
		if st.button("Click here, We paid for you"):
			create_usertable()
			add_userdata(link,a,b)
			st.warning("Thank you, We will check your transaction and process your request")
			st.warning("Your Request will be processed in less than 1 hr")	



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
			plann=st.selectbox("Dear, Admin These are the Links to the Plans",("Views","No_Refill-Followers","Refill-Followers","Likes","Free_Views"))
			if plann == "Views":
				st.write("https://socialdaddy.in/default.aspx?cat=55")
				st.write("Select this -> 1.Insagram Views 2.Instagram Views [Working Instant]- 2 INR")
			elif plann == "No_Refill-Followers":
				st.write("https://socialdaddy.in/default.aspx?cat=55")
				st.write("Select this -> 1.Instagram Followers(No-Refill) 2.Instagram Followers [10k Per Day] [Instant]- 78 INR")
				
			elif plann == "Refill-Followers":
				st.write("https://socialdaddy.in/default.aspx?cat=55")
				st.write("Select this -> 1.Instagram Followers(Refill) 2.Instagram Followers [Real Users 2k Per Day] [15Days Refill]- 328 INR")
				
			elif plann == "Likes":
				st.write("https://socialdaddy.in/default.aspx?cat=55")
				st.write("Select this -> 1.Instagram Likes 2.Instagram Likes [15k] [Working After Update]- 57 INR")
				
			elif plann == "Free_Views":
				st.write("https://famoid.com/get-free-instagram-views/")
				
				
				
			
			
				
				
				
			
			
		
		




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
	var_a=st.radio("",["Views","Followers","Likes","Free Views"])
	v_dic={1:"100 Views - 4 INR",2:"1000 Views - 5 INR",3:"10000 Views - 15 INR",4:"100000 Views - 150 INR"}
	if var_a == "Views":
		st.subheader("2. Select the plan")
		
		v_plan=st.radio("",["100 Views - 4 INR","1000 Views - 5 INR","10000 Views - 15 INR","100000 Views - 150 INR"])
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("","+91- ")
	        buff=insta_link(v_plan,ph_no)
					    
	elif var_a == "Followers":
		v_plan=""
		st.subheader("2. Select the plan")
		p=st.radio("",["No Refill - Followers will not be added if decreased","Refill - Followers will be added again if decreased in next 15 days"])
		if p == "No Refill - Followers will not be added if decreased":
			v_plan=st.radio("",["50 Followers - 7 INR","100 Followers - 12 INR","200 Followers - 22 INR","400 Followers - 40 INR","500 Followers - 60 INR","1,000 Followers - 100 INR"])
		elif p == "Refill - Followers will be added again if decreased in next 15 days":
			v_plan=st.radio("",["100 Followwers - 39 INR","200 Followers - 78 INR","300 Followers - 115 INR","500 Followers - 193 INR","1000 Followers - 386 INR"])
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("","+91- ")
		buff=insta_link(v_plan,ph_no)			 
		#st.warning("{} is selected".format(v_plan))
	elif var_a == "Likes":
		st.subheader("2. Select the plan")
		
		v_plan=st.radio("",["100 Likes - 9 INR","200 Likes - 17 INR","300 Likes - 24 INR","400 Likes - 31 INR","500 Likes - 38 INR","1000 Likes - 73 INR"])
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("","+91- ")
		buff=insta_link(v_plan,ph_no)
					
					
	else:
		st.subheader("2. You will get free views on your last uploaded video.")
		st.info("We are paying for you. So, that you trust, use and share our website")
		
		v_plan="100 Free Views"
		st.warning("{} is selected".format(v_plan))
		st.subheader("3. Enter your Phone number and relax, we will contact you shortly")
		ph_no=st.text_input("","+91- ")
		buff=insta_link(v_plan,ph_no)
					
			 
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






















