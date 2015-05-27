Summary:	PostgreSQL Config Tuner
Name:		pgtune
Version:	0.9.4
Release:	1%{?dist}
License:	BSD
Group:		Applications/Databases
URL:		http://pgfoundry.org/projects/pgtune
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:	http://pgfoundry.org/frs/download.php/2445/%{name}-%{version}.tar.gz
Patch0:		pgtune-settingsdir.patch
Requires:	postgresql-server
Buildarch:	noarch

%description
pgtune takes the wimpy default postgresql.conf and expands the database server
to be as powerful as the hardware it is being deployed on.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/%{name}

install -m 755 pgtune %{buildroot}%{_bindir}
install -m 644 -p pg_settings* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc TODO COPYRIGHT
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%attr(755,root,root) %{_bindir}/pgtune

%changelog
* Wed Oct 28 2009 Devrim Gunduz <devrim@commandprompt.com> 0.9.1-1
- Initial packaging for PostgreSQL RPM Repository
* Wed Oct 28 2009 Greg Smith <gsmith@gregsmith.com> 0.9.2-1
- Added copyright file, does not install sample postgresql.conf file.
* Wed March 14 2014 Eric Litwin <elitwin@rocketmail.com> 0.9.3
- Cleanup formatting to support 80 column display
* Fri March 14 2014 Eric Litwin <elitwin@rocketmail.com> 0.9.3
- Allow version to be targeted via command line argument
* Fri March 14 2014 Eric Litwin <elitwin@rocketmail.com> 0.9.3
- Allow version to be targeted via command line argument
* Mon March 17 2014 Eric Litwin <elitwin@rocketmail.com> 0.9.3
- pep8 compliance and added 9.3 settings
* Wed May 27 2015 Eric Litwin <elitwin@rocketmail.com> 0.9.4
- Added support for 9.4 and changed default version
