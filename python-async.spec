%define 	module	async
Summary:	Async Framework
# Name must match the python module/package name (as in 'import' statement)
Name:		python-%{module}
Version:	0.6.1
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/a/async/%{module}-%{version}.tar.gz
# Source0-md5:	6f0e2ced1fe85f8410b9bde11be08587
URL:		https://github.com/gitpython-developers/async
BuildRequires:	python-devel
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
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

%{__rm} -r $RPM_BUILD_ROOT%{py_sitedir}/async/{AUTHORS,README,test}

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{py_sitedir}/async
%dir %{py_sitedir}/async/mod
%{py_sitedir}/async/*.py[co]
%{py_sitedir}/async/mod/*.py[co]
%attr(755,root,root) %{py_sitedir}/async/mod/*.so
%{py_sitedir}/async-*.egg-info
