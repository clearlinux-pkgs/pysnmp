#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pysnmp
Version  : 4.3.0
Release  : 18
URL      : https://pypi.python.org/packages/source/p/pysnmp/pysnmp-4.3.0.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pysnmp/pysnmp-4.3.0.tar.gz
Summary  : SNMP library for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pysnmp-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
PYTHON SNMP FRAMEWORK
---------------------
This is a pure-Python, open source and free implementation of v1/v2c/v3
SNMP engine.

%package python
Summary: python components for the pysnmp package.
Group: Default

%description python
python components for the pysnmp package.


%prep
%setup -q -n pysnmp-4.3.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
