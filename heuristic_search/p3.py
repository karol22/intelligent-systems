import matplotlib.pyplot as plt 
import matplotlib.image as img


LAMBDA = 0.1
def cost(I, X):
    ans = 0.0

    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            ans += 0.5*( (X[i][j]-I[i][j])**2)
            if(i-1>=0):
                ans+= LAMBDA*0.5*( (X[i][j]-X[i-1][j])**2)
            if(j-1>=0):
                ans+= LAMBDA*0.5*( (X[i][j]-X[i][j-1])**2)
            if(i+1<I.shape[0]):
                ans+= LAMBDA*0.5*( (X[i][j]-X[i+1][j])**2)
            if(j+1<I.shape[1]):
                ans+= LAMBDA*0.5*( (X[i][j]-X[i][j+1])**2)
    return ans

        

# Load image
im1 = img.imread('house.png')
im2 = img.imread('city.png')


# Get pixel values
I = im1[:,:,1]
X = im2[:,:,1]

print("Lambda: ", LAMBDA)
print("The cost is: ", cost(I, X))
plt.imshow(im1) 
plt.show()
plt.imshow(im2) 
plt.show()
