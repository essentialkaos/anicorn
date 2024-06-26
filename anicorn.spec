################################################################################

Summary:    Simple utility for starting/restarting Unicorn
Name:       anicorn
Version:    2.1.10
Release:    0%{?dist}
Group:      Applications/System
License:    Apache License, Version 2.0
URL:        https://kaos.sh/anicorn

Source0:    https://source.kaos.st/%{name}/%{name}-%{version}.tar.bz2

BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:   %{name} = %{version}-%{release}

################################################################################

%description
Simple utility for starting/restarting Unicorn.

################################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

################################################################################

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_bindir}/%{name}

################################################################################

%changelog
* Tue Jun 11 2024 Anton Novojilov <andy@essentialkaos.com> - 2.1.10-0
- Improved automatic disabling of color output usage

* Thu Nov 30 2023 Anton Novojilov <andy@essentialkaos.com> - 2.1.9-0
- Code refactoring

* Fri Jan 04 2019 Anton Novojilov <andy@essentialkaos.com> - 2.1.8-0
- Code refactoring

* Thu Aug 30 2018 Anton Novojilov <andy@essentialkaos.com> - 2.1.7-0
- Fixed getting PID from empty PID file

* Fri Jul 06 2018 Gleb Goncharov <g.goncharov@fun-box.ru> - 2.1.6-0
- Fixed bug with checking dead process if it is a Unicorn

* Wed Jul 04 2018 Gleb Goncharov <g.goncharov@fun-box.ru> - 2.1.5-0
- Fixed bug with trying to restart Unicorn when it is dead and PID file exists

* Fri Jun 22 2018 Anton Novojilov <andy@essentialkaos.com> - 2.1.4-0
- Fixed bug with handling command line arguments

* Thu Jun 21 2018 Anton Novojilov <andy@essentialkaos.com> - 2.1.3-0
- Fixed bug with handling a huge amount of arguments

* Sun Feb 11 2018 Anton Novojilov <andy@essentialkaos.com> - 2.1.2-0
- Fixed bug with trying to use PID of dead Unicorn process when PID file exists

* Fri Nov 10 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.1-0
- Fixed bug with killing old Unicorn master by the watchdog before sending
  QUIT signal
- Removed useless log message from watchdog

* Thu Nov 09 2017 Anton Novojilov <andy@essentialkaos.com> - 2.1.0-0
- Improved Unicorn restart resilience
- Fixed bug with starting watchdog

* Thu Nov 09 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.1-0
- Minor improvements

* Wed Nov 08 2017 Anton Novojilov <andy@essentialkaos.com> - 2.0.0-0
- Added shutdown watchdog mode
- Improved Unicorn restart sequence

* Mon Oct 30 2017 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Improved compatibility with Unicorn
- Minor improvements

* Fri Oct 27 2017 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- Initial release
