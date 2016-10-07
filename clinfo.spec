Name:           clinfo
Version:        2.1.16.01.12
Release:        1%{?dist}
Summary:        Enumerate OpenCL platforms and devices

License:        Public Domain
URL:            https://github.com/Oblomov/clinfo
Source0:        https://github.com/Oblomov/clinfo/archive/%{version}.tar.gz

BuildRequires:  opencl-headers
BuildRequires:  opencl-icd-loader-devel


%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).


%prep
%setup -q


%build
%configure || :
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_bindir}
install -m0755 clinfo %{buildroot}/%{_bindir}/

mkdir -p %{buildroot}/%{_mandir}/man1
cp -a man/clinfo.1 %{buildroot}/%{_mandir}/man1/


%files
%doc README LICENSE
%{_bindir}/clinfo
%{_mandir}/man1/clinfo.1.gz


%changelog
* Fri Oct 07 2016 Jajauma's Packages <jajauma@yandex.ru> - 2.1.16.01.12-1
- Public release
