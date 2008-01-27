%define name	exempi
%define version	1.99.8
%define release	%mkrel 1

%define major		3
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		%{name}
Summary:	XMP implementation
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	BSD-like
URL:		http://libopenraw.freedesktop.org/wiki/Exempi
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz
Source1:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.gz.asc
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	expat-devel
BuildRequires:	boost-devel

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

%package -n %{develname}
Summary:	XMP implementation - development libraries and headers
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Exempi is an implementation of XMP. It is based on Adobe XMP SDK
4.1.1. The API is C based and means to be used from any language and
be easier to maintain ABI stability.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/%{name}-2.0
%{_libdir}/*.*a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
