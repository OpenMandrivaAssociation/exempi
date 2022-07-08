%define major 8
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	XMP implementation
Name:		exempi
Version:	2.6.2
Release:	1
Group:		System/Libraries
License:	BSD-like
Url:		http://libopenraw.freedesktop.org/wiki/Exempi
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(zlib)

%description
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%package -n %{libname}
Summary:	XMP implementation
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%package -n %{devname}
Summary:	XMP implementation - development libraries and headers
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%prep
%setup -q

%build
%configure \
	--disable-static

%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?.*

%files -n %{libname}
%{_libdir}/libexempi.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
