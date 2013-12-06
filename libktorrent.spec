%define major	5
%define libname %mklibname ktorrent %{major}
%define devname %mklibname ktorrent -d

Name:		libktorrent
Version:	1.3.1
Release:	4
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://ktorrent.org/downloads/4.3.1/%{name}-%{version}.tar.bz2
BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(qca2)

%description
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%package common
Summary:	Common files of libktorrent
Group:		System/Libraries

%description common
Common files for libktorrent, used by KTorrent, a BitTorrent program for
KDE.

%package -n %{libname}
Summary:	Ktorrent libbrary
Group:		System/Libraries
Requires:	%{name}-common >= %{version}-%{release}

%description -n %{libname}
KTorrent is a BitTorrent program for KDE. It's main features are:
 o Downloads torrent files
 o Upload speed capping, seeing that most people can't upload
   infinite amounts of data.
 o Internet searching using  The Bittorrent website's search engine
 o UDP Trackers

%package -n %{devname}
Summary:	Ktorrent plugin devel headers
Group:		Networking/File transfer
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	libktorrent-devel < 1.3.1-2

%description -n %{devname}
Ktorrent plugin devel headers.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

%files common -f %{name}.lang

%files -n %{libname}
%{_kde_libdir}/libktorrent.so.%{major}*

%files -n %{devname}
%{_kde_includedir}/*
%{_kde_appsdir}/cmake/*/*
%{_kde_libdir}/*.so

