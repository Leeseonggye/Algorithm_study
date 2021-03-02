#!/usr/bin/env python
# coding: utf-8

# ## Calculator

# In[12]:


class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# ## Calculator with constructor

# In[20]:


class FourCal:
    def __init__(self, first = 0, second = 1):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


# In[25]:


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result


# In[26]:


a = MoreFourCal(2,5)


# In[27]:


a.pow()

