#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import os
import time
class asc_change():
	def __init__(self,pic_id):
		asc_change.pic_id=pic_id
	@classmethod
	def start(self):
		res=""
		next_pic_id=asc_change.pic_id
		while next_pic_id!="0":
			tail,next_pic_id=asc_change.find(next_pic_id,3)
			res+=str(tail[0])
			print ("res:"+res,"next_pic_id",next_pic_id)
			continue
			if next_pic_id=="0":
				break
		return res

	@classmethod
	def find(self,pic_id,times):
		n=times
		patten3=re.compile("...$")
		patten2=re.compile("..$")
		patten1=re.compile(".$")
		if n==3:
			third=patten3.findall(pic_id)
			if third:
				if int(third[0])>123:
					next_re=asc_change.find(pic_id,n-1)
					return next_re
				else:
					next_pic_id=asc_change.cut_down(pic_id,3)
					return chr(int(third[0])),next_pic_id
			else:
				next_pic_id=asc_change.cut_down(pic_id,3)
				next_re=asc_change.find(pic_id,n-1)
				return next_re,next_pic_id

		if n==2:
			third=patten2.findall(pic_id)
			if third:
				next_pic_id=asc_change.cut_down(pic_id,2)
				return chr(int(third[0])),next_pic_id
			else:
				next_pic_id=asc_change.cut_down(pic_id,2)
				next_re=asc_change.find(pic_id,n-1)
				return next_re,next_pic_id
		if n==1:
			third=patten1.findall(pic_id)
			if third:
				next_pic_id=asc_change.cut_down(pic_id,1)
				return chr(int(third[0])),next_pic_id
			else:
				print("you should input string!")
				return
	@classmethod
	def cut_down(self,pic_id,times):
		n=times
		if n==3:
			next_pic_id=str(int(int(pic_id)/1000))
			return next_pic_id
		if n==2:
			next_pic_id=str(int(int(pic_id)/100))
			return next_pic_id
		if n==1:
			next_pic_id=str(int(int(pic_id)/10))
			return pic_id

a=asc_change("107107107")
res=a.start()
print (res)
