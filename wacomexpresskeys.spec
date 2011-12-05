%define	tarname		expresskeys

Name:		wacomexpresskeys
Version:	0.4.2
Release:	3%{?dist}
Summary:	Wacom ExpressKeys and Touch Strips configuration utility

Group:		System Environment/Base
License:	GPLv2+
URL:		http://expresskeys.ruivo.org/
Source0:	http://expresskeys.ruivo.org/%{tarname}-%{version}.tar.gz

BuildRequires:	libX11-devel, libXi-devel, xorg-x11-server-devel, libXext-devel, libXtst-devel
Requires:	xorg-x11-server-Xorg, linuxwacom
ExcludeArch:	s390 s390x

%description
Configuration utility to bind Wacom tablet's ExpressKeys and Touch Strips to
generate other input events.

%prep
%setup -q -n %{tarname}-%{version}

%build
%configure

export CFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS ChangeLog NEWS README TODO USAGE
%{_bindir}/expresskeys

%changelog
* Tue Sep 29 2009 Jarod Wilson <jarod@redhat.com> 0.4.2-3
- Add USAGE to %%doc (#525546)

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 14 2009 Jarod Wilson <jarod@redhat.com> 0.4.2-1
- Update to 0.4.2
- Submit for Fedora package review

* Wed Apr 09 2008 Aristeu Rozanski <arozansk@redhat.com> 0.4.1-1
- initial version for RHEL-5

