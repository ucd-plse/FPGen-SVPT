Name: gsl
Summary: GNU Scientific Library (GSL)
Packager: jungman@lanl.gov, rosalia@lanl.gov
%define version 2.0
%define release 0
Version: %{version}
Release: %{release}
License: GPL
Vendor: The GSL Team
Distribution: research software
Source: gsl-%{version}.tar.gz
Group: Libraries/Research
%define mybuildroot /var/tmp/%{name}-build
BuildRoot: %{mybuildroot}

%description
  The GNU Scientific Library (GSL) is a numerical library for C and
C++ programmers.  It contains over 1000 mathematical routines written
in ANSI C.  The library follows modern coding conventions, and lends
itself to being used in very high level languages (VHLLs).

The library covers the following subject areas:

  Complex Numbers             Roots of Polynomials     Special Functions
  Vectors and Matrices        Permutations             Sorting
  BLAS Support                Linear Algebra           Eigensystems
  Fast Fourier Transforms     Quadrature               Random Numbers
  Quasi-Random Sequences      Random Distributions     Statistics
  Histograms                  N-Tuples                 Monte Carlo Integration
  Simulated Annealing         Differential Equations   Interpolation
  Numerical Differentiation   Chebyshev Approximation  Series Acceleration
  Discrete Hankel Transforms  Root-Finding             Minimization
  Least-Squares Fitting       Physical Constants       IEEE Floating-Point

Further information can be found in the GSL Reference Manual.
Copyright (C) 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005,
2006, 2007 The GSL Team.

Install the gsl package if you need a library for high-level
scientific numerical analysis.

%prep
%setup -q -n gsl-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=%{_prefix} \
    --bindir=%{_bindir} --mandir=%{_mandir} \
    --localstatedir=%{_localstatedir} --libdir=%{_libdir} \
    --datadir=%{_datadir} --includedir=%{_includedir} \
    --sysconfdir=%{_sysconfdir}
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{_prefix} bindir=$RPM_BUILD_ROOT%{_bindir} \
    mandir=$RPM_BUILD_ROOT%{_mandir} libdir=$RPM_BUILD_ROOT%{_libdir} \
    localstatedir=$RPM_BUILD_ROOT%{_localstatedir} \
    datadir=$RPM_BUILD_ROOT%{_datadir} \
    includedir=$RPM_BUILD_ROOT%{_includedir} \
    sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc {NEWS,ChangeLog,INSTALL,README,AUTHORS,THANKS,SUPPORT,BUGS}
%doc /usr/info/*
/usr/bin/gsl-config
/usr/bin/gsl-histogram
/usr/bin/gsl-randist
/usr/lib
/usr/include/gsl
/usr/share/aclocal/gsl.m4
/usr/share/man
