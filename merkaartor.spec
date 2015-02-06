Summary:	Openstreetmap mapping program
Name:		merkaartor
Version:	0.18.1
Release:	4
License:	GPLv2+
Group:		Sciences/Other
Url:		http://merkaartor.be/projects/merkaartor/
Source0:	http://merkaartor.be/attachments/download/301/%{name}-%{version}.tar.bz2
BuildRequires:	gdb
BuildRequires:	qt4-linguist
BuildRequires:	boost-devel
BuildRequires:	gdal-devel
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(QtWebKit)

%description
Merkaartor is an openstreetmap (http://www.openstreetmap.org) mapping
program. Merkaartor focuses on providing a visually pleasing but
performant editing environment for free geographical data.

%files -f %{name}.lang
%doc AUTHORS CHANGELOG CREDITS TODO
%{_bindir}/*
%{_datadir}/%{name}/*.xml
%{_datadir}/applications/*.desktop
%{_libdir}/%{name}/plugins/background/*.so
%{_libdir}/%{name}/plugins/styles/libskulpture.so
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
lrelease translations/merkaartor*.ts
%qmake_qt4 \
	PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	TRANSDIR_MERKAARTOR=%{_datadir}/%{name}/translations \
	TRANSDIR_SYSTEM=%{qt4dir}/translations \
	GDAL=1
%make

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}

%find_lang %{name} --with-qt

rm -f %{buildroot}/merkaartor.gdb-index

