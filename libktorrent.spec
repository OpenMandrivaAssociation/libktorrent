Name:		libktorrent
Version:	1.3.0
Release:	1
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/4.2.1/%{name}-%{version}.tar.bz2
BuildRequires:	gmp-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	qca2-devel >= 2.0.1
BuildRequires:	libgcrypt-devel
BuildRequires:	boost-devel

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

#-------------------------------------------------------------------------

%package common
Summary:	Common files of libktorrent
Group:		System/Libraries

%description common
Common files for libktorrent, used by KTorrent, a BitTorrent program for
KDE.

%files common -f %{name}.lang
#-------------------------------------------------------------------------

%define ktorrent_major 5
%define libktorrent %mklibname ktorrent %{ktorrent_major}

%package -n %{libktorrent}
Summary:	Ktorrent libbrary
Group:		System/Libraries
Requires:	libktorrent-common >= %{version}

%description -n %{libktorrent}
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -n %{libktorrent}
%{_kde_libdir}/libktorrent.so.%{ktorrent_major}*

#-------------------------------------------------------------------------

%package devel
Summary:	Ktorrent plugin devel headers
Group:		Networking/File transfer
Requires:	%{libktorrent} = %{version}-%{release}

%description devel
Ktorrent plugin devel headers.

%files devel
%{_kde_includedir}/*
%{_kde_appsdir}/cmake/*/*
%{_kde_libdir}/*.so

#-------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%changelog
* Wed Jun 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.2.1-1
+ Revision: 807177
- version update 1.2.1

* Tue Mar 06 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.2.0-1
+ Revision: 782324
- Update to 1.2.0

* Thu Jan 12 2012 Andrey Smirnov <asmirnov@mandriva.org> 1.1.1-2
+ Revision: 760421
- spec for updated Russian translation
- Updated Russian translation

* Thu Apr 28 2011 Funda Wang <fwang@mandriva.org> 1.1.1-1
+ Revision: 659822
- new version 1.1.1

* Wed Mar 16 2011 Funda Wang <fwang@mandriva.org> 1.1.0-1
+ Revision: 645474
- 1.1.0 final

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 1.1-0.rc1.1
+ Revision: 636453
- new version 1.1 rc1

* Wed Dec 29 2010 Funda Wang <fwang@mandriva.org> 1.0.5-1mdv2011.0
+ Revision: 625975
- new version 1.0.5

* Mon Oct 18 2010 Funda Wang <fwang@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 586558
- new version 1.0.4

* Mon Aug 30 2010 Funda Wang <fwang@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 574252
- new version 1.0.3

* Sat Jul 10 2010 Anssi Hannula <anssi@mandriva.org> 1.0.2-2mdv2011.0
+ Revision: 550161
- split localization to libktorrent-common to avoid file conflicts
  (Andrey Borzenkov)

* Sat Jul 10 2010 Funda Wang <fwang@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 549947
- new libmajor
- new version 1.0.2

* Tue Jun 15 2010 Funda Wang <fwang@mandriva.org> 1.0.1-1mdv2010.1
+ Revision: 548052
- New version 1.0.1

* Tue May 25 2010 Funda Wang <fwang@mandriva.org> 1.0.0-1mdv2010.1
+ Revision: 545839
- New version 1.0.0
- drop unneeded BRs

* Tue May 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0-0.rc1.1mdv2010.1
+ Revision: 542004
- import libktorrent

