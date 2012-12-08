%define name	exempi
%define version	2.1.1
%define release	%mkrel 6

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
#Patch0:		exempi-2.1.0-gcc44.patch
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
#%patch0 -p1 -b .gcc44

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


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-4mdv2011.0
+ Revision: 664158
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-3mdv2011.0
+ Revision: 605109
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-2mdv2010.1
+ Revision: 522577
- rebuilt for 2010.1

* Mon Aug 10 2009 Emmanuel Andry <eandry@mandriva.org> 2.1.1-1mdv2010.0
+ Revision: 414315
- New version 2.1.1
- drop gcc patch

  + Christophe Fergeau <cfergeau@mandriva.com>
    - fix compilation with gcc 4.4

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 2.1.0-2mdv2009.1
+ Revision: 324631
- New upstream release

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.99.8-2mdv2009.0
+ Revision: 220732
- rebuild

* Sun Jan 27 2008 Funda Wang <fwang@mandriva.org> 1.99.8-1mdv2008.1
+ Revision: 158881
- new major
- New version 1.99.8

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Adam Williamson <awilliamson@mandriva.org>
    - Import exempi

