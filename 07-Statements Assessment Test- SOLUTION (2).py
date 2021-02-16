#!/usr/bin/env python
# coding: utf-8

# # Statements Assessment Test
# Let's test your knowledge!

# _____
# **Use <code>for</code>, .split(), and <code>if</code> to create a Statement that will print out words that start with 's':**

# In[1]:





# In[13]:


St = 'Print only the words that start with s in this sentence Said monney'
List = St.split()
for i in List:
    if i.startswith('s'):
        print(i)
        
    if i.startswith('m'):
        print(i)

        


# In[ ]:





# ______
# **Use range() to print all the even numbers from 0 to 10.**

# In[15]:


for i in range(0,11):
    if i%2==0:
        print(i)


# ___
# **Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.**

# In[113]:


l = list(range(1,51))
# print (l)
d = [i for i in l if i%3==0] 
print (d)


# _____
# **Go through the string below and if the length of a word is even print "even!"**

# In[74]:


st = 'Print every word in this sentence that has an even number of letters'
l = st.split(' ')

#1 To print seperate words
#     print(st)

#2 To iterate in words of string 
for word in l: 
#    print(word)

#3 if length is even 
    if len(word)%2==0:
        print(word)


# In[ ]:





# ____
# **Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".**

# In[105]:


for i in range (1,20):
#     print(i,end="")
    if i%3==i%5==0:
        print("Fizz Buzz")
    
    elif i%3==0:
        print("Fizz")
    
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        
    


# ____
# **Use List Comprehension to create a list of the first letters of every word in the string below:**

# In[92]:


st = 'Create a list of the first letters of every word in this string'


# In[115]:


st = 'Create a list of the first letters of every word in this string'
st = st.split()
for i in st:
    print(i[0],end="  , ")


# In[112]:


pwd


# ### Great Job!
