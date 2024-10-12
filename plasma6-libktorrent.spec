#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define major 6
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define libname %mklibname KTorrent6
%define devname %mklibname KTorrent6 -d

Name:		plasma6-libktorrent
Version:	24.08.2
Release:	%{?git:0.%{git}.}1
Summary:	BitTorrent program for KDE
Group:		Networking/File transfer
License:	GPLv2+
Url:		http://ktorrent.org/
%if 0%{?git:1}
Source0:	https://invent.kde.org/network/libktorrent/-/archive/%{gitbranch}/libktorrent-%{gitbranchd}.tar.bz2#/libktorrent-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/libktorrent-%{version}.tar.xz
%endif
BuildRequires:	boost-devel
BuildRequires:	gmp-devel
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	cmake(Qca-qt6)

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
Requires:	cmake(KF6Archive)
Requires:	cmake(KF6Config)
Requires:	cmake(KF6KIO)
Requires:	cmake(Qt6Core)
Requires:	cmake(Qt6Network)
Requires:	boost-devel
Requires:	gmp-devel
Requires:	pkgconfig(libgcrypt)

%description -n %{devname}
Ktorrent plugin devel headers.

%prep
%autosetup -p1 -n libktorrent-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
# do not build non-installed example binary
sed -i -e "/add_subdirectory(examples)/d" CMakeLists.txt

%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build

%find_lang libktorrent6

%files common -f libktorrent6.lang

%files -n %{libname}
%{_libdir}/libKTorrent6.so.%{major}*
%{_libdir}/libKTorrent6.so.%(echo %{version}|cut -d. -f1)*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/cmake/KTorrent6/
%{_libdir}/*.so
