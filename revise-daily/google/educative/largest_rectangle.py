
import math

def largest_rect_brute_force(heights):
     for i in range(1, len(heights)):
          for j in range(i):
               width = i - j
               height = min(heights[i], heights[j])
     return

def largest_rectangle(heights):

     stack = []
     max_area = -math.inf
     for i, h in enumerate(heights+[0]):
          while stack and h < heights[stack[-1]]:
               height = heights[stack.pop()]
               width = i if not stack else i - stack[-1] - 1
               max_area = max(height*width, max_area)
          stack.append(i)
     return max_area
