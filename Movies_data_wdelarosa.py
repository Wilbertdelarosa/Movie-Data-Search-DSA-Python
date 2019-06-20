#Wilbert M. De la Rosa

#CSC 110 - Programming Project - Spring	2019

#Movie	Data

#Due: 4/30/2019

#Instructor: Dr. Lisa DiPippo

#--------------------------------------------------------------------------------
#This program will go through a movie data file, which contains information such as:
#the title, genre, run time, rating, Studio, Year of movies released from 2000 to 2009
#The user can select between 8 options to find specific data of the file.
#--------------------------------------------------------------------------------

# Function to open a file - using exception handling
def openFile():
    goodFile = False
    while goodFile == False:
        fname = input("Enter name of output file: ")

        # Begin exception handling
        try:
            # Try to open the file using the name given
            moviesFile = open(fname, 'r')

            # If the name is valid, set Boolean to true to exit loop
            goodFile = True
   
        except IOError:
            # If the name is not valid - IOError exception is raised
            print("Invalid file name, please try again...")

    #Returns the file
    return moviesFile


# Function to get the lists of data - returns all the list from the data movie
def getData():
    #Open the movie file
    moviesFile = openFile()

    #Lists that will have the corresponding data
    titleList = []
    genreList = []
    runtimeList = []
    ratingList = []
    studioList = []
    yearList = []

    
    line = moviesFile.readline()
    line = line.strip()
    line = moviesFile.readline()

    #Read,split, and strip the lines and add to the lists
    while line != "":
        line = line.strip()
        title,genre,runtime,rating,studio,rel_year = line.split(",")
        titleList.append(str(title))
        genreList.append(str(genre))
        runtimeList.append(int(runtime))
        ratingList.append(str(rating))
        studioList.append(str(studio))
        yearList.append(int(rel_year))
        line = moviesFile.readline()
        
    #Close the file
    moviesFile.close()

    #Returns all the lists
    return titleList, genreList, runtimeList, ratingList, studioList, yearList


#Choice 1
#Function to find all films of a certain genre
def genreFun(genreList):
    alist = []
    option = False

    #User enters the genre name until it is correct if the genre is not there user needs to enter again
    while option ==False:
        genre = input("Enter genre: ")
        if genre in genreList:
            option = True
        else:
            print("Invalid name, please try again...")

    #Find all the genres with the same name in the genreList and add the index in aList
    for i in range(len(genreList)):
                if genreList[i] == genre:
                    alist.append(i)
                    
    #Returns all the index with the specific genre                
    return alist


#Choice 2
#Function that finds all films with a certain rating
def ratingFun(ratingList):
    rlist = []
    option = False

    #User enters the rating name until it is correct if the rating is not there user needs to enter again
    while option ==False:
        rating = input("Enter rating: ")
        if rating in ratingList:
            option = True
        else:
            print("Invalid name, please try again...")

    #Find all the rating with the same name in the ratingList and add the index in rList
    for i in range(len(ratingList)):
        if ratingList[i] == rating:
          rlist.append(i)

    #Returns all the index with the specific rating      
    return rlist


#Choice 3
#Function to find Find the longest film made by a specific studio
def longestfilmFun(runtimeList,studioList):
    ind = []
    list2 = []

    option = False
    
    #User enters the studio name until it is correct if the studio is not there user needs to enter again
    while option ==False:
        studio = input("Enter studio: ")
        if studio in studioList:
            option = True
        else:
            print("Invalid name, please try again...")
            
    #Add to ind list all the studios with that name
    for i in range(len(studioList)):
        if studio == studioList[i]:
            ind.append(i)
            
    #Find the runtime of every studio in list in and add it to list 2     
    for i in range(len(ind)):
        list2.append(runtimeList[ind[i]])

    #Find the highest runtime in list 2
    long = list2[0]
    for i in range(len(list2)):
        if list2[i] > long:
            long = list2[i]

    #The position of the long runtime        
    pos = ind[list2.index(long)]
    return pos



#Choice 4
#Function that search for a film by title
def titleFun(titleList):
    option = False

    #User enters the title name until it is correct if the title is not there user needs to enter again
    while option ==False:
        title = input("Enter the title: ")
        if title in titleList:
            option = True
        else:
            print("Invalid name, please try again...")

    #Find the movie with by the title in the title list       
    for i in range(len(titleList)):
        if title == titleList[i]:
            index = i

    #Returns the index of the movie        
    return index



    
#Choice 5
#Fin average runtime of films made in a given year
def runtimeRange(runtimeList,yearList):
    #Empty list that will have the index of every year in the range enter
    list1 = []

    #Empy list that will have the runtime of the times the years appears in yearList
    list2 = []
    
    option = False
    
    # Begin exception handling to enter the correct years
    while option == False:
        try:
            year1 = int(input("Enter year 1(oldest year first): "))
            year2 = int(input("Enter year 2: "))
            if (year1 and year2) in yearList and year1 < year2:
                option = True
            elif year2 < year1:
                print("The second year needs to be after year 1")
            else:
                print("Invalid name, please try again...")

        # If the years is not valid - exception is raised
        except ValueError:
            print("Invalid name, please try again...")

    #Create a new varible for the print statement at the end, because year1 get to the same value as year2 in the for loop
    year1forprint = year1
    
    #Add to list1 the index of the year range enter from the yearlist
            
    while year1 < year2:
        for i in range(len(yearList)):
            if year1 == yearList[i]:
                list1.append(i)
        #Increase the year until year1 is less than year2
        year1 += 1
        
    
    #Add all the runtime values of every index from list1    
    for i in range(len(list1)):
        list2.append(runtimeList[list1[i]])
        
    #sum all the values from list 2    
    add = sum(list2)

    #Finds the average of the sum of all the runtimes
    average = round(add/len(list2),1)
    
    print("The average runtime for films made between ", year1forprint, " and ", year2, "is", average)
    return 


#choice 6
#Sort all lists	by runtime and	write the results to a new file
def runWrites(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    outName = input("Enter name of output file: ")
    outFile = open(outName, 'w')

    #Creates a copy of the runtimeList
    runewList = runtimeList.copy()

    #List that will contain the index of every runtime sorted
    indList = []

    #Use the (Algorithm of selection sort) to sort the runewList(the copy list)
    #This algorithm compares pair of numbers and move the smallest to the left
    for i in range(0, len(runewList)):            
        min = i
        for j in range(i + 1, len(runewList)):
            
            if runewList[j] < runewList[min]:
                min = j

        runewList[i], runewList[min] = runewList[min], runewList[i]

    #Find the index of the runtime sorted from the runtimeList and add it to indList   
    for i in range(len(runewList)):
        indList.append(runtimeList.index(runewList[i]))
        
     #Insert all the movies with the runtime sorted
    for i in range(len(runewList)):
        outFile.write(str(titleList[indList[i]]).ljust(40) + str(genreList[indList[i]]).ljust(14) + str(runewList[i]).ljust(5) + str(ratingList[indList[i]]).ljust(8) + str(studioList[indList[i]]).ljust(25) + str(yearList[indList[i]]).ljust(25) + '\n')

    #Close the file    
    outFile.close()
    return


#Choice 7 - Extra Credit
#Function to find the studio that has produced the most films

def findstudio(studioList):
    
    #Empty list that will include every studio just one time
    list1 = []

    #Empty list that will include the amount of time the studio is repeated
    list2 = []
    
    #Initialize counter for the amount of time a studio appears
    count = 0

    #Find every studio in the studio list and add it to list1
    for i in range(len(studioList)):
        if studioList[i] not in list1:
            list1.append(studioList[i])

    #Algorithm of nested loop to find the amount of times the studios in list1 appears in studiolist(That has all the data)
    #and when every counter finish is added to list 2
    for i in range(len(list1)):
        count = 0
        for j in range(len(studioList)):
            if list1[i] == studioList[j]:
                count = count + 1
        list2.append(count)

    #Find the highest number in list2 which means studio that has appear the most times
    #Finds the index for the studio
    highest = list2[0]
    for i in range(len(list2)):
        if highest < list2[i]:
            highest = list2[i]
            index = i

    #Prints the studio with most movies created        
    print("The studio that has created most movies is ",list1[index]) 
    return 

#Function that has all the print statements to the user decided and make a choice
def firstprints():
    print("Please Choose one of the following options")
    print("1 - Find all films of a certain genre")
    print("2 - Find all films with a certain rating")
    print("3 - Find the longest film made by a specific studio")
    print("4 - Search for a film by title")
    print("5 - Find the average runtime of films made in a given year range")
    print("6 - Sort all lists by runtime and write the results to a new file")
    print("7 - Studio that has produced the most films")
    print("8 - Quit")

    #User enter the choice 
    choice = int(input("Enter the number of your choice: "))

    #Returns the number selected
    return choice


def main():
    #Call the get data function that returns the lists
    titleList, genreList, runtimeList, ratingList, studioList, yearList = getData()

    #Call the prints to make the choice
    choice = firstprints()

    #Call the functions to find all films of a certain genre
    if choice == 1:
        #call the function with the genre index list
        alist = genreFun(genreList)

        print("The Films that meet your criteria are:")
        print("")
        print(("TITLE").ljust(40),("GENRE").ljust(14),("TIME").ljust(5),("RATING").ljust(8),("STUDIO").ljust(25),("YEAR").ljust(25))

        #Print all the movies by genre in columns using ljust()
        for i in range(len(alist)):
            print(str(titleList[alist[i]]).ljust(40), str(genreList[alist[i]]).ljust(14), str(runtimeList[alist[i]]).ljust(5) , str(ratingList[alist[i]]).ljust(8) , str(studioList[alist[i]]).ljust(25) , str(yearList[alist[i]]).ljust(25))

    
    elif choice == 2:
        #call the function with the rating index list
        rlist = ratingFun(ratingList)
        
        print("")
        print("The Films that meet your criteria are:")
        print("")
        print(("TITLE").ljust(40),("GENRE").ljust(14),("TIME").ljust(5),("RATING").ljust(8),("STUDIO").ljust(25),("YEAR").ljust(25))

        #Print all the movies by rating in columns using ljust()
        for i in range(len(rlist)):
            print(str(titleList[rlist[i]]).ljust(40) , str(genreList[rlist[i]]).ljust(14) , str(runtimeList[rlist[i]]).ljust(5) , str(ratingList[rlist[i]]).ljust(8) , str(studioList[rlist[i]]).ljust(25) , str(yearList[rlist[i]]).ljust(25))

               
    elif choice == 3:
        #Call the function that returns the index of the studio with most movies created 
        pos = longestfilmFun(runtimeList,studioList)
        
        print("The Films that meet your criteria are:")
        print("")
        print(("TITLE").ljust(40),("GENRE").ljust(14),("TIME").ljust(5),("RATING").ljust(8),("STUDIO").ljust(25),("YEAR").ljust(25))

        #Print the movie with the studio with most movies created in columns using ljust()
        print(str(titleList[pos]).ljust(40) , str(genreList[pos]).ljust(14) , str(runtimeList[pos]).ljust(5) , str(ratingList[pos]).ljust(8) , str(studioList[pos]).ljust(25) , str(yearList[pos]).ljust(25))

    
    elif choice == 4:
        #Call the function with the index of the title entered 
        title = titleFun(titleList)
        print("")
        print("The Films that meet your criteria are:")
        print("")
        print(("TITLE").ljust(40),("GENRE").ljust(14),("TIME").ljust(5),("RATING").ljust(8),("STUDIO").ljust(25),("YEAR").ljust(25))

        #Print the film in columns using ljust()
        print(str(titleList[title]).ljust(40) , str(genreList[title]).ljust(14) , str(runtimeList[title]).ljust(5) , str(ratingList[title]).ljust(8) , str(studioList[title]).ljust(25) , str(yearList[title]).ljust(25))


    
    elif choice == 5:
        #Call the function to find the average runtime of films made in a given year range
        runtimeRange(runtimeList,yearList)

                      
    elif choice == 6:
        #Sort all lists by runtime and write the results to a new file 
        runWrites(titleList, genreList, runtimeList, ratingList, studioList, yearList)

    
    elif choice == 7:
        #call the function with the studio that has produced the most films
        findstudio(studioList)

                     
    elif choice == 8:
        #Quit the program
        import sys
        sys.exit()
   
