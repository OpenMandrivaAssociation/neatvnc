%define major 0
%define libname %mklibname neatvnc
%define devname %mklibname neatvnc -d

Name: neatvnc
Version: 0.9.2
Release: 2
Source0: https://github.com/any1/neatvnc/archive/refs/tags/v%{version}.tar.gz
Summary: VNC server library
URL: https://github.com/any1/neatvnc
License: ISC
Group: System/Libraries
BuildRequires: meson
BuildRequires: ninja
BuildRequires: pkgconfig(nettle)
BuildRequires: pkgconfig(gmp)
BuildRequires: pkgconfig(gbm)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(gnutls)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libturbojpeg)
BuildRequires: pkgconfig(aml)

%description
VNC server library.

%package -n %{libname}
Summary: VNC server library
Group: System/Libraries

%description -n %{libname}
VNC server library.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
