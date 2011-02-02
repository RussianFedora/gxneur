Summary:	GTK wrapper for X Neural Switcher
Name:		gxneur
Version:	0.12.0
Release:	1%{?dist}

Group:		User Interface/Desktops
License:	GPLv2
URL:		http://www.xneur.ru
Source:		http://dists.xneur.ru/release-%{version}/tgz/%{name}-%{version}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	GConf2-devel
BuildRequires:	gtk2-devel
BuildRequires:	xneur-devel = %{version}
BuildRequires:	desktop-file-utils
BuildRequires:	pcre-devel
BuildRequires:	aspell-devel
BuildRequires:	libglade2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	enchant-devel

Requires:	xneur = %{version}


%description
GTK wrapper for X Neural Switcher. It's program like Punto
Switcher, but has other functionally and features.


%prep
%setup -q


%build
# Avoid lib64 rpaths
%if "%{_libdir}" != "/usr/lib"
sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure
%endif
sed -i 's!Core!Core;!g' %{name}.desktop.in

export LDFLAGS="-lX11 -ldl"
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%find_lang %{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog NEWS
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_mandir}/man?/*


%changelog
* Wed Feb  2 2011 Arkady L. Shane <ashejn@yandex-team.ru> 0.12.0-1
- update to 0.12.0

* Sun Nov 28 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.11.1-1
- update to 0.11.1

* Thu Oct  6 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.10.0-1
- update to 0.10.0

* Fri May 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.9-1
- update to 0.9.9

* Sun Mar 21 2010 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.8-1
- update to 0.9.8

* Thu Oct 15 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.7-1
- update to 0.9.7

* Wed Sep 16 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.6-1
- update to 0.9.6

* Wed Aug  5 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.5-1
- update to 0.9.5

* Wed Apr 21 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.4-1
- 0.9.4

* Fri Apr 17 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.4-0.1.20090414svn345
- last snapshot

* Fri Jan  9 2009 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.3-1
- update to 0.9.3

* Mon Nov 10 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.2-1
- update to 0.9.2

* Fri Jul 25 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.1-1
- 0.9.1

* Tue Jun 24 2008 Arkady L. Shane <ashejn@yandex-team.ru> 0.9.0-1
- 0.9.0

* Fri Oct 12 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.8.0-1
- 0.8.0
- add BR aspell-devel

* Tue Jul 17 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.6.2-1
- 0.6.2

* Fri May 18 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.6.1-1
- 0.6.1

* Mon Apr 23 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.6-1
- 0.6.0

* Sat Mar 10 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.5-1
- 0.5.0

* Tue Jan 23 2007 Arkady L. Shane <ashejn@yandex-team.ru> 0.4.0-1
- rebuild for FC6
- cleanup spec

* Fri Jan 5 2007 Nik <niktr@mail.ru>
- adopted spec from ALT for FC6
- updated to svn version dated 03012007
- minor changes in spec and desktop files

* Thu Dec 21 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1
- new version (0.3.0)

* Sun Oct 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.0_1-alt1
- initial build for Sisyphus
