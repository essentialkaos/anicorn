###############################################################################

Summary:         Simple utility for starting/restarting Unicorn
Name:            anicorn
Version:         1.1.0
Release:         0%{?dist}
Group:           Applications/System
License:         EKOL
URL:             https://github.com/essentialkaos/anicorn

Source0:         https://source.kaos.io/%{name}/%{name}-%{version}.tar.bz2

BuildArch:       noarch
BuildRoot:       %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:        %{name} = %{version}-%{release}

###############################################################################

%description
Simple utility for starting/restarting Unicorn.

###############################################################################

%prep
%setup -q

%build
%install
rm -rf %{buildroot}

install -dm 755 %{buildroot}%{_bindir}
install -pm 775 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE.EN LICENSE.RU
%{_bindir}/%{name}

###############################################################################

%changelog
* Mon Oct 30 2017 Anton Novojilov <andy@essentialkaos.com> - 1.1.0-0
- Improved compatibility with Unicorn
- Minor improvements

* Fri Oct 27 2017 Anton Novojilov <andy@essentialkaos.com> - 1.0.0-0
- Initial release
