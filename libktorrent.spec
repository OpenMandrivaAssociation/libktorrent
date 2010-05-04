%define rev rc1

Name: libktorrent
Version: 1.0
Release: %mkrel 0.%rev.1
Summary: BitTorrent program for KDE
Group: Networking/File transfer
License: GPLv2+
Url: http://ktorrent.org/
Source0: http://ktorrent.org/downloads/%{version}/%{name}-%{version}%{rev}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gmp-devel
BuildRequires: kdepimlibs4-devel
BuildRequires: kdebase4-workspace-devel
BuildRequires: qca2-devel >= 2.0.1
BuildRequires: boost-devel
BuildRequires: taglib-devel

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

#-------------------------------------------------------------------------

%define ktorrent_major 1
%define libktorrent %mklibname ktorrent %ktorrent_major

%package -n %libktorrent
Summary:    Ktorrent libbrary
Group:      System/Libraries

%description -n %libktorrent
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%files -n %libktorrent -f %name.lang 
%defattr(-,root,root)
%_kde_libdir/libktorrent.so.%{ktorrent_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer
Requires: %{libktorrent} = %{version}

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%{_kde_includedir}/*
%{_kde_appsdir}/cmake/*/*
%{_kde_libdir}/*.so

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version%rev

%build
%cmake_kde4 
%make
 
%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name}

%clean
rm -rf %buildroot

