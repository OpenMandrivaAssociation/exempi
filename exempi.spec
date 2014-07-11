%define major	3
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d

Summary:	XMP implementation
Name:		exempi
Version:	2.1.1
Release:	13
Group:		System/Libraries
License:	BSD-like
Url:		http://libopenraw.freedesktop.org/wiki/Exempi
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
Source1:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz.asc

BuildRequires:	boost-devel
BuildRequires:	pkgconfig(expat)

%description
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%package -n %{libname}
Summary:	XMP implementation
Group:		System/Libraries

%description -n %{libname}
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%package -n %{devname}
Summary:	XMP implementation - development libraries and headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libexempi.so.%{major}*

%files -n %{devname}
%{_includedir}/%{name}-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
