This is a project I had done during my visit at International Centre for Theoretical Physics (ICTP), Trieste, Italy.

# Block-structured-random-matrices

![Motivation](https://github.com/lingminhao/Block-structured-random-matrices/blob/main/readme-images/projectmotivation.png)

Initially, Random Matrix Theory (RMT) was born due to Eugene Wigner in physics. It serves as a powerful statistical model to study large systems with network structure. Biological systems like gene regulatory network, protein-protein interaction network and ecological system network are usually large and complex. Thus RMT can be applied in its full potential to extract important information about them. Block-structured random matrix is a more realistic model to study the ecosystem of modular organization. To study the stability of an ecosystem, it suffices to know the rightmost eigenvalue of the random matrix. One naive method is to generate all eigenvalue by brute force and locate the rightmost eigenvalue. But this demands high time complexity as S grows. In this project, we will see how random matrix theory sheds a light to optimize this problem. 

## Summary of Results

Here we modelled an example of synthetic huge biological system with 1000 species, 5 within system interactions using a random matrix. The coordinate axes represents the real and imaginary value of the eigenvalues. 

As we can see below, we can find the eigenvalues by brute force (blue dots) or by using the results we derived using methodology from statistical physics (red lines + red dots). It is not surprising because 1000 is a relatively small number. 

![example](https://github.com/lingminhao/Block-structured-random-matrices/blob/main/readme-images/example.png)

When we changed to model a huge biological system with 10000 species, the computer we used from ICTPs' with i7 processors and 8gb rams starts to perform poorly. Since we are only concerned with the rightmost eigenvalues, our methodology gives an accurate approximation (red lines + red dots). This method is way faster and efficient compared to brute force approach. Refer to [Report.pdf](https://github.com/lingminhao/Block-structured-random-matrices/blob/main/Report.pdf) to understand the theory behind this method.  

![advantage](https://github.com/lingminhao/Block-structured-random-matrices/blob/main/readme-images/advantage.png)

## How to run the code 
Step 1: Read [Report.pdf](https://github.com/lingminhao/Block-structured-random-matrices/blob/main/Report.pdf) to understand the terminology. 

Step 2: Open all python files.

Step 3: Run BlockMatrices.py (you can change the values of the parameters).


Note that this code is only valid for biological systems that follows Gaussian distribution. You can change the distribution by modifying the function "SampleNormal" in BuildMatrices.py
