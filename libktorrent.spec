%define major	6
%define libname %mklibname ktorrent %{major}
%define devname %mklibname ktorrent -d

Name:		libktorrent
Version:	2.0
Release:	1.1
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
Source0:	http://download.kde.org/stable/ktorrent/5.0/%{name}-%{version}.tar.xz
BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	extra-cmake-modules
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
# our qca pkg config is in a non standard path due to qt5/4 split
export PKG_CONFIG_PATH=%{_libdir}/qt4/pkgconfig

# Gentoo workaround because gmp.h in MULTILIB_WRAPPED_HEADERS is breaking this
sed -i -e "/^find_package/ s/\"\${LibGMP_MIN_VERSION}\" //" \
	CMakeLists.txt
sed -i -e "/^find_dependency/ s/ \"@LibGMP_MIN_VERSION@\"//" \
	LibKTorrentConfig.cmake.in

# do not build non-installed example binary
sed -i -e "/add_subdirectory(examples)/d" CMakeLists.txt

%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name}

%files common -f %{name}.lang

%files -n %{libname}
%{_kde5_libdir}/libktorrent.so.%{major}*

%files -n %{devname}
%{_kde5_includedir}/*
%{_kde5_libdir}/cmake/LibKTorrent/
%{_kde5_libdir}/*.so

