%define module	numarray

Name:           python-%{module}
Version:        1.5.2
Release:        %mkrel 7
Summary:        Numarray: array processing for numbers, strings, records and objects

Group:          Development/Python
License:        BSD-like
URL:            https://www.stsci.edu/resources/software_hardware/numarray/
Source0:        http://dl.sourceforge.net/sourceforge/numpy/%{module}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  python-devel

%description
Numarray is an array processing package designed to efficiently
manipulate large multi-dimensional arrays.  Numarray is modelled after
Numeric and features c-code generated from python template scripts,
the capacity to operate directly on arrays in files, and improved type
promotions.  Numarray provides support for manipulating arrays
consisting of numbers, strings, records, or objects using the same
basic infrastructure and syntax.

%package	devel
Summary:	Numarray Library C bindings
Group:		Development/Python
Requires:	%{name} = %{version}

%description	devel
Install this to develop C bindings against the Numarray Python library.

%prep
%setup -n %{module}-%{version} -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
PYTHONDONTWRITEBYTECODE= \
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT --record=INSTALLED_OBJECTS.tmp

# Ghost optimized 
sed 's/\(.*\.pyo\)/%ghost \1/' < INSTALLED_OBJECTS.tmp >INSTALLED_OBJECTS

# Move development files
sed "s#%{_includedir}/python%{pyver}/numarray.*##" < INSTALLED_OBJECTS > INSTALLED_OBJECTS.tmp
mv INSTALLED_OBJECTS.tmp INSTALLED_OBJECTS

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_OBJECTS
%defattr(-,root,root,-)
%doc *.txt

%files devel
%defattr(-,root,root,-)
%{_includedir}/python%{pyver}/numarray
%doc *.txt


