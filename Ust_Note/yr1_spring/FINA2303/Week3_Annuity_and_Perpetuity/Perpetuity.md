## Definition
An asset that generates a constant cash flows $C$ forever.
## Present Value
The PV formula is
$$
PV_{0}=\sum_{r=1}^T\frac{C_{t}}{(1+r)^t}
$$
With a constant $C$, it becomes
$$
PV_{0}=C\times \sum_{r=1}^T\frac{1}{(1+r)^t}=\frac{\frac{C}{1+r}\left( 1-\frac{1}{(1+r)^T} \right)}{1-\frac{1}{1+r}}
$$
Since $C$ is paid forever,
$$
PV_{0}=\lim_{ T \to \infty } \frac{\frac{C}{1+r}\left( 1-\frac{1}{(1+r)^T} \right)}{1-\frac{1}{1+r}}=\frac{C}{r}
$$
## Growing Perpetuity
