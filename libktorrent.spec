%define major 6
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname KF5Torrent %{major}
%define devname %mklibname KF5Torrent -d

Name:		libktorrent
Version:	23.08.5
Release:	2
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		https://ktorrent.org/
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(qca2-qt5)

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
Requires:	%{name}-common >= %{EVRD}
Obsoletes:	%{mklibname libtorrent 6} < 2.1-1
Provides:	%{mklibname libtorrent 6} = 2.1-1
Conflicts:	%{mklibname libtorrent 6} < 2.1-1

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
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Obsoletes:	%{_lib}ktorrent-devel < 2.1-1
Conflicts:	%{mklibname libtorrent -d} < 2.1
Requires:	cmake(KF5Archive)
Requires:	cmake(KF5Config)
Requires:	cmake(KF5KIO)
Requires:	cmake(Qt5Core)
Requires:	cmake(Qt5Network)
Requires:	boost-devel
Requires:	gmp-devel
Requires:	pkgconfig(libgcrypt)

%description -n %{devname}
Ktorrent plugin devel headers.

%prep
%setup -q

%build
# our qca pkg config is in a non standard path due to qt5/4 split
export PKG_CONFIG_PATH=%{_libdir}/qt4/pkgconfig

# Gentoo workaround because gmp.h in MULTILIB_WRAPPED_HEADERS is breaking this
sed -i -e "/^find_package/ s/\"\${LibGMP_MIN_VERSION}\" //" \
	CMakeLists.txt
sed -i -e "/^find_dependency/ s/ \"@LibGMP_MIN_VERSION@\"//" \
	KF5TorrentConfig.cmake.in

# do not build non-installed example binary
sed -i -e "/add_subdirectory(examples)/d" CMakeLists.txt

%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}5

%files common -f %{name}5.lang

%files -n %{libname}
%{_kde5_libdir}/libKF5Torrent.so.%{major}*
%{_kde5_libdir}/libKF5Torrent.so.%(echo %{version}|cut -d. -f1)*

%files -n %{devname}
%{_kde5_includedir}/*
%{_kde5_libdir}/cmake/KF5Torrent/
%{_kde5_libdir}/*.so
