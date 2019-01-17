# ParallelProgrammingPractice
Repository used for practicing parallel programming techniques 

## Array processing
This example aims to demonstrate a parallel approach to processing a two dimmensional array of elements with size n x m. A function is evaluated on each array element. The computation on each element is independent from other array elements. For simplicity a simple function which performs the the addition of each element of the array and keeps a total sum. 
The problem is computationally intensice.

![Array processing picture](https://computing.llnl.gov/tutorials/parallel_comp/images/array_proc1.gif)

Serial pseudocode for this problem
```
do j = 1,n
  do i = 1,n
    a(i,j) = fcn(i,j)
  end do
end do
```

[Source](https://computing.llnl.gov/tutorials/parallel_comp/#Concepts)

## PI calculation
The value of PI can be calculated in various ways. Consider the Monte Carlo method of approximating PI:  
Inscribe a circle with radius r in a square with side length of 2r  
The area of the circle is Πr2 and the area of the square is 4r2  
The ratio of the area of the circle to the area of the square is:  
Πr2 / 4r2 = Π / 4  
If you randomly generate N points inside the square, approximately   
N * Π / 4 of those points (M) should fall inside the circle.  
Π is then approximated as:  
N * Π / 4 = M  
Π / 4 = M / N  
Π = 4 * M / N  
Increasing the number of points generated improves the approximation.   

![PI calculation image](https://computing.llnl.gov/tutorials/parallel_comp/images/pi1.gif)

Serial pseudocode for this problem:
```
npoints = 10000
circle_count = 0

do j = 1,npoints
  generate 2 random numbers between 0 and 1
  xcoordinate = random1
  ycoordinate = random2
  if (xcoordinate, ycoordinate) inside circle
  then circle_count = circle_count + 1
end do

PI = 4.0*circle_count/npoints
```

[Source](https://computing.llnl.gov/tutorials/parallel_comp/#Concepts)
