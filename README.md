Numerical integration for multidimensional integrals
===

![Demo](/public/out.gif)

### Overview

There are several reasons for carrying out numerical integration, as opposed to analytical integration by finding the antiderivative:
* The integrand $f(x)$ may be known only at certain points, such as obtained by sampling. Some embedded systems and other computer applications may need numerical integration for this reason
* A formula for the integrand may be known, but it may be difficult or impossible to find an antiderivative that is an elementary function. An example of such an integrand is $f(x) = e^{−x^2}$, the antiderivative of which (the error function, times a constant) cannot be written in elementary form

When dealing with the numerical integration of functions of many variables, one could face many challenges

* Arbitrary shape of the area (against the interval in one-dismensional case)
* The need for much more dots while computing for a more accurate approximation
* Difficulty in assessing errors and dispersion of values

While we can't solve it in generale case, knowing the function beforehand could help us to compute the error and needed values

### Computing

I was using [`Sparse grid`](https://en.wikipedia.org/wiki/Sparse_grid) method for computing. We can approximate the integral over an admissible set $G$ (custom area set by user), by calculating integral sums for some partition of the bar $I: G \subset I$. To minimize error, we should choose minimal $I$ that contains given area

Mean value $f(x, y)$ continuous in the region
D of the function $f(x, y)$ according to the `Mean value theorem` is represented by the expression

$\overline{f}(x,y) = \frac{1}{S}\iint\limits_G f(x,y) dxdy, S = (x_{1}-x_{0})(y_{1}-y_{0})$

Assuming that the average value is approximately equal to the value of the function
in the center of the rectangle: $f(x, y) ≈ f(x, y)$, where $x = (a + b)/2, y = (c + d)/2$

We obtain a formula for the approximate calculation of the double integral

$\iint\limits_G f(x,y) dxdy \approx Sf(\overline{x}, \overline{y})$

### Error evaluation

Let's find the error as the difference between the value of the function according to the Taylor formula and our sum. Now we introduce a partition, with an increase in the fineness of which we obtain a completely sane error


### Build

```bash
sudo apt install python3-tk
pip install -r requirements.txt
python3 main.py
```

### Resources

http://hoster.bmstu.ru/~fn1/wp-content/uploads/2011/08/uchebno-metod/Blumin_Fed_Hrap_chisl_met.pdf

https://en.wikipedia.org/wiki/Numerical_integration#Multidimensional_integrals

http://mathprofi.ru/dvoinye_integraly_dlya_chainikov.html

