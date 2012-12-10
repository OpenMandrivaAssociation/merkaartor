Name:		merkaartor
Version:	0.18.1
Release:	1
License:	GPLv2+
URL:		http://merkaartor.be/projects/merkaartor/
BuildRequires:	qt4-devel >= 4.4
BuildRequires:	qt4-linguist
BuildRequires:	libexiv-devel gdal-devel
BuildRequires:	boost-devel
BuildRequires:	gdb
Source0:	http://merkaartor.be/attachments/download/301/%{name}-%{version}.tar.bz2
Group:		Sciences/Other
Summary:	Openstreetmap mapping program

%description
Merkaartor is an openstreetmap (http://www.openstreetmap.org) mapping
program. Merkaartor focuses on providing a visually pleasing but
performant editing environment for free geographical data.

%prep
%setup -q

%build
lrelease translations/merkaartor*.ts
%qmake_qt4 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	TRANSDIR_MERKAARTOR=%_datadir/%{name}/translations \
	TRANSDIR_SYSTEM=%qt4dir/translations \
	GDAL=1
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
%find_lang %{name} --with-qt
rm -f %{buildroot}/merkaartor.gdb-index

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%_datadir/%{name}/*.xml
#%_datadir/%{name}/world_background.osb
%_datadir/applications/*.desktop
%{_libdir}/%{name}/plugins/background/*.so
%{_libdir}/%{name}/plugins/styles/libskulpture.so
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%doc AUTHORS CHANGELOG CREDITS TODO


%changelog
* Tue Jan 31 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.17.2-1mdv2012.0
+ Revision: 769994
- new version 0.17.2

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.15.3-2mdv2011.0
+ Revision: 612850
- the mass rebuild of 2010.1 packages

* Fri Apr 16 2010 Frederik Himpe <fhimpe@mandriva.org> 0.15.3-1mdv2010.1
+ Revision: 535633
- Update to new version 0.15.3

* Fri Aug 14 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14-1mdv2010.0
+ Revision: 416397
- Fix libdir
- Update to new version 0.14
- Fix string format

* Mon Jun 08 2009 Michael Scherer <misc@mandriva.org> 0.13.2-3mdv2010.0
+ Revision: 384144
- update to latest release

* Sun Jan 04 2009 Funda Wang <fwang@mandriva.org> 0.12-3mdv2009.1
+ Revision: 324536
- rebuild

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.12-2mdv2009.1
+ Revision: 303633
- fix url

* Sun Nov 16 2008 Funda Wang <fwang@mandriva.org> 0.12-1mdv2009.1
+ Revision: 303628
- add desktop file
- import merkaartor


