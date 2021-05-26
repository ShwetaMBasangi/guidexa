
"""
Dictionaries
"""

import speech_recognition as speech
import pyttsx3
import pygame

#Initialize the Speech Generation Library
engine=pyttsx3.init()
engine.setProperty('rate',200)

#Initialize Pygame
pygame.init()

#Create Screen with size 900x600
width=900
height= 600
screen=pygame.display.set_mode( ( width, height) )

#Set a Title of Screen
pygame.display.set_caption('GuidEXA')

#Display the Background Image
bg=pygame.image.load("images/bg1.jpg").convert_alpha()
image1=pygame.transform.scale(bg, (900,600))
screen.blit(image1,(0,0))
pygame.display.update()

places={"sinhagad": ["sng","Sinhagad is a hill fortress located at around 35 km southwest of the city of Pune, India. Some of the information available at this fort suggests that the fort could have been built 2000 years ago. The caves and the carvings in the Kaundinyeshwar temple stand as proofs for the same.The Sinhagad (Lion's Fort) was strategically built to provide natural protection due to its very steep slopes. The walls and bastions were constructed only at key places. There are two gates to enter the fort, the Kalyan Darwaza and Pune Darwaza which are positioned at the south east and north-east ends respectively.[2] The fort was also strategically located at the centre of a string of other Maratha Empire forts such as Rajgad Fort, Purandar Fort and Torna Fort"],
          "bedekar misal":["misal","Punekar loves this place for its own unique Misal, one of the famous food place in Pune. Bedekar  misal has been serving tasty spicy Misal in consistent way for more than six decades since 1948.Its been more than six decades and having a trendy fan following in Pune.Bedekar Missal has its own sole taste unlike the other spicy Misal in Pune or rest of Maharashtra. Mixed with crispy sev,onions and awesome homemade masala, the Misal is quite spicy and sweet which is again pretty gripping. What’s even more attractive is the fact that the owner gives more importance to their quality and taste and that’s why you can see they still serve it with sliced bread by default instead of the Pavs."],
          "raja Dinkar Kelkar Museum":["kelkar","The Raja Dinkar Kelkar Museum is in Pune, Maharashtra, India.[1] It contains the collection of Dr. Dinkar G. Kelkar (1896–1990), dedicated to the memory of his only son, Raja.[2] The three-storey building houses various sculptures dating back to the 14th century.[citation needed] There are also ornaments made of ivory, silver and gold, musical instruments (a particularly fine collection),[3] war weapons and vessel."],
          "pataleshwar Cave Temple":["pataleshwar","The Pataleshwar Cave Temple (also called Panchaleshvara or Bamburde) is a rock-cut cave temple, carved out in the 8th century in the Rashtrakuta period by Kannadiga kings.[1] It is located in what is now Pune, in the state of Maharashtra, India. It was originally situated outside the town, but the city limits have expanded so that it is now located on the downtown Jangali Maharaj Road. It has been declared as a protected monument by the government"],
          "saras baug":["saras","Deemed as the favorite place for most of the Pune people, Sarasbaug is an important landmark that features a temple, and lake amidst manicured gardens. Its longstanding popularity is all because of the Ganesha temple in the park - Talyatla Ganpati. Even the park becomes the center of attraction for many migratory birds. Earlier, when the park was in making process, Sarus crane was quite prominent, and that perhaps the reason why it is called Sarasbaug."],
          "Dagaduseth Halwai Ganapati Temple":["ganpati","Shreemant Dagadusheth Halwai Ganapati Temple in Pune is dedicated to the Hindu God Ganesh. The temple is popular in Maharashtra and is visited by over hundred thousand pilgrims every year.[1][2] Devotees of the temple include celebrities and Chief Ministers of Maharashtra who visit during the annual ten-day Ganeshotsav festival.[3] The main Ganesh idol is insured for sum of ₹10 million (US$140,000).[4] The temple celebrated 125 years of its Ganapati in the year 2017"],
          "shaniwar wada":["shanivar","Shaniwarwada is a historical fortification in the city of Pune in Maharashtra, India. Built in 1732, it was the great seat of the Peshwas of the Maratha Empire until 1818, when the Peshwas lost control to the British East India Company after the Third Anglo-Maratha War. Following the rise of the Maratha Empire, the palace became the center of Indian politics in the 18th century"],
          "Karla Caves":["karla","The Karla Caves, Karli Caves, Karle Caves or Karla Cells, are a complex of ancient Buddhist Indian rock-cut caves at Karli near Lonavala, Maharashtra. It is just 10.9 Kilometers away from Lonavala. Other caves in the area are Bhaja Caves, Patan Buddhist Cave, Bedse Caves and Nasik Caves. The shrines were developed over the period – from the 2nd century BCE to the 5th century CE. The oldest of the cave shrines is believed to date back to 160 BCE, having arisen near a major ancient trade route, running eastward from the Arabian Sea into the Deccan."],
          "Aga Khan Palace":["aga","The Aga Khan Palace was built by Sultan Muhammed Shah Aga Khan III in Pune, India. The palace was an act of charity by the spiritual leader of the Nizari Ismaili Muslims, who wanted to help the poor in the neighbouring areas of Pune, who were drastically hit by famine."],
          "katraj zoo":["katraj","The Rajiv Gandhi Zoological Park, commonly known as the Rajiv Gandhi Zoo or Katraj Zoo,[3] is located in Katraj, Pune district, Maharashtra State, India. It is managed by the Pune Municipal Corporation. The 130-acre (53 ha) zoo is divided into three parts: an animal orphanage, a snake park, and a zoo, and includes the 42-acre (17 ha) Katraj Lake"],
          "Osho ashram":["osho","The Osho Ashram now known as the OSHO International Meditation Resort in Pune is an iconic landmark located in Koregaon Park. Pune was the birthplace of the movement led by Rajneesh Chandra Mohan Jain Osho who propagated the teachings and philosophy of one’s sexuality and spirituality. We bet you’ve all seen the Netflix docu-series called ‘Wild Wild Country’ (if not, please do!) where many scenes of his followers building the Ashram in 1947 have been clearly captured to understand. But, here’s a fun fact, it is not actually an ashram, it is actually a meditation centre. It focuses on multiple meditative techniques like Osho Kundalini meditation, Osho Nataraj, and Osho Nadabrahma, to name a few."]}
answer="No"
activate="none"
exitstatus="no"

while True:
    try:
        pygame.display.update()
        for event in pygame.event.get():
            #Event to Quit Pygame Window
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            #To Read whether 'c' key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    activate = 'c'
                    print("c pressed")
                    
                    
        #If 'c' key is pressed
        if activate=='c':
            #Change the background image to Listening Image
            listenImg=pygame.image.load("images/bg.jpg").convert_alpha()
            image1=pygame.transform.scale(listenImg, (900,600))
            screen.blit(image1,(0,0))
            pygame.display.update()
            
            #Start Listening the User Voice Input
            r=speech.Recognizer()
            
            with speech.Microphone() as source:
                    r.adjust_for_ambient_noise(source)
                    print("Speak:")
                    audio=r.listen(source)
                #Convert Voice Commands to Text
            command=r.recognize_google(audio).lower()
                
            print("You said: "+command)
            
            #Search each keyword in the dictionary one-by-one
            for keyword in places:
                
                #if one of the keyword in the dictionary is in 
                #User Input
                if keyword in command:
                               image=pygame.image.load("images/"+places[keyword][0]+".jpg").convert_alpha()
                               image1=pygame.transform.scale(image, (900,600))
                               screen.blit(image1,(0,0))
                               pygame.display.update()
                               
                               engine.runAndWait()
                               engine.say(places[keyword][1])
                               engine.runAndWait()
       

           
            if exitstatus=="yes":
                    pygame.quit()
                    break
            #Reset the UI to get further inputs    
            activate="none" 
            bg=pygame.image.load("images/bg1.jpg").convert_alpha()
            image1=pygame.transform.scale(bg, (900,600))
            screen.blit(image1,(0,0))
        
    #Stop Taking Voice Commands
    except speech.UnknownValueError:
        print("Could not understand audio")
    except speech.RequestError as e:
        print("Could not request results; {0}".format(e))
    except KeyboardInterrupt:
        break
    

           
                
