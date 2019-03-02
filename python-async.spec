%define 	module	async
Summary:	Async Framework
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	0.6.2
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/a/async/%{module}-%{version}.tar.gz
# Source0-md5:	9b06b5997de2154f3bc0273f80bcef6b
URL:		https://github.com/gitpython-developers/async
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Async is a framework to process interdependent tasks in a pool of
workers.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%dir %{py_sitescriptdir}/async
%{py_sitescriptdir}/async/*.py[co]
%{py_sitescriptdir}/async-*.egg-info
%{py_sitescriptdir}/async/test
