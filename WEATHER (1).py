import sys
print(" \t\tWelcome to Weather on the Go! \n\tYour personalized website for all flood updates")
print("________________________________________________________________________________________________________________________________________________________________")
print()
print("Please choose from the following region of the world: ")
print("Note: 1.Please avoid the serial numbers and choose the required region \n      2.Avoid typing all information in brackets\n      3.We request you to avoid spelling errors of the area you choose.")
print("1. Domestic (states in India)")
print("2. International")
s1= input("Enter choice: ")
s1= s1.lower()
print()
if(s1=="domestic"):
    st= input("Please choose either state or Union Territory :")
    st=st.lower()
    if(st=="state"):
        print("Choose any one of the following states: ")
        print("1. Andhra Pradesh \n2. Arunachal Pradesh\n3. Assam \n4. Bihar \n5. Chhattisgarh")
        print("6. Goa \n7. Gujarat\n8. Haryana\n9. Himachal\n10. Jharkhand")
        print("11. Karnataka\n12. Kerala\n13. Madhya\n14. Maharashtra\n15. Manipur")
        print("16. Meghalaya\n17. Mizoram \n18. Nagaland\n19. Odisha \n20. Punjab")
        print("21. Rajasthan\n22. Sikkim \n23. Tamil Nadu\n24. Telangana \n25. Tripura")
        print("26. Uttar Pradesh\n27. Uttarakhand \n28. West Bengal")
    elif(st=="union territory"):
        print("Choose any one of the Union Territories: ")
        print("1.Andaman and Nicobar Islands \n2.Chandigarh \n3.Dadra and Nagar Haveli \n4.Daman and Diu \n5.Delhi")
        print("6.Jammu, and Kashmir \n7.Ladakh \n8.Lakshadweep \n9.Puducherry")
    else:
        sys.exit("Invalid input")
        

if(s1=="international"):
    print("1.Africa \n2.Antarctica \n3.Asia \n4.Australia \n5.Europe \n6.North America \n7.South America")
    print()
    cont= input("Choose the continent in which your desired country is located: ")
    cont= cont.lower()
    if(cont=="africa"):
        print("1.Chad  \n2.Congo \n3.Egypt \n4.Ethiopia \n5.Kenya")
        print("6.Libya \n7.Madagascar \n8.Mauritius \n9.Morocco \n10.Namibia")
        print("11.Nigeria \n12.Rwanda \n13.Senegal \n14.Somalia \n15.South Africa")
        print("16.Tanzania \n17.Uganda  \n18.Wakanda \n19.Zimbabwe")
    elif(cont=="antarctica"):
        print()
    elif(cont=="asia"):
        print("1.Afghanistan \n2.Bangladesh \n3.Bhutan \n4.China \n5.Indonesia \n6.Iran")
        print("7.Iraq \n8.Israel \n9.Japan \n10.Kuwait  \n11.Malaysia \n12.Maldives")
        print("13.Myanmar \n14.Nepal \n15.North Korea  \n16.Oman \n17.Pakistan \n18.Philippines")
        print("19.Qatar \n20.Russia  \n21.Saudi arabia \n22.Singapore \n23.South korea \n24.Sri Lanka")
        print("25.Syria \n26.Thailand \n27.UAE \n28.Ukraine \n29.Vietnam \n30.Yemen")
    elif(cont=="australia"):
        print("1.Australia \n2.Fiji \n3.New Zealand \n4.Papua New Guinea \n5.Tonga")
    elif(cont=="europe"):
        print("1.Austria \n2.Belgium \n3.Croatia \n4.Denmark  \n5.France \n6.Germany")
        print("7.Greece \n8.Iceland \n9.Italy \n10.Netherlands \n11.Norway \n12.Portugal")
        print("13.Spain \n14.Sweden \n15.Switzerland  \n16.Turkey \n17.United Kingdom")
    elif(cont=="south america"):
        print("1.Argentina \n2.Bolivia \n3.Brazil \n4.Chile \n5.Colombia")
        print("6.Ecuador \n7.Paraguay \n8.Peru \n9.Uruguay \n10.Vanezuela")
    elif(cont=="north america"):
        print("1.Antigua and Barbuda \n2.Bahamas \n3.Canada \n4.Costa Rica \n5.Cuba")
        print("6.Hondurus \n7.Jamaica \n8.Mexico \n9.Panama \n10.United States of America")
    else:
        sys.exit("Invalid input")
        
        
country= input("Enter desired area: ")
country= country.lower()






    
    
    
    


        



