# TODO:
# - fix description
# ** mpg123 plugin are removed, so alsaplayer play mp3 only via mad plugin
# ** add info about new subpackages (scopes, interface-gtk and others)
# - add output-jack plugin (requires jackit.sf.net)
# - add input-flac plugin (requires flac.sf.net)
# - think about static libalsaplayer.a (add --enable-static to %%configure and make subpackage)
# - add/check translations
Summary:	Alsaplayer - MP2/MP3/WAV/CD player
Summary(pl):	Alsaplayer - odtwarzacz MP2/MP3/WAV/CD
Name:		alsaplayer
Version:	0.99.72
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.alsa-project.org/pub/people/andy/%{name}-%{version}.tar.bz2
Patch0:		%{name}-nas.patch
Patch1:		%{name}-docs.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	curl-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	mad-devel
BuildRequires:	nas-devel
BuildRequires:	OpenGL-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_pkglibdir	%{_libdir}/%{name}
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
AlsaPlayer is a new type of PCM player. It is heavily multi-threaded
and tries to excercise the ALSA library and driver quite a bit.
Features include:

Input addons:
 - MP2 and MP3 support
 - Ogg Vorbis support (subpackage)
 - WAV support, 8-, 16-bit, mono, stereo, any sample rate
 - CDDA support, CD Digital Audio playback! and thus USB ready :)
 - Also plays files mapped by audiofs (CDDA)
 - MAD MPEG audio
 - Module support (mikmod) (subpcakage)

Output addons:
 - ALSA. Best supported of course :) (subpackage)
 - OSS. Kernel native sound drivers
 - Sparc. UltraSparc sound drivers
 - SGI. SGI audio library driver
 - ESD. Enlightened sound daemon support (subpackage)
 - NAS. Network Audio System (subpakcage)
 - null :-)

Visual scopes:
 - Stereoscope
 - Monoscope
 - Levelmeter
 - Spacescope
 - FFTscope
 - FFTscope II
 - More being developed...

General features:
 - Full speed (pitch) control, positive *and* negative! (First Linux
   player that does this!! MP3's and CD's do varispeed :)
 - Queue (playlist) support
 - Concurrent visual scopes (open as many as you want)
 - Multi-threaded design for efficient/skip free playback (RT)
 - GUI Interface based on gtk+
 - NOGUI operation for shell script usage
 - Plug-in core architecture
 - Low latency mode, as low as 5ms when scheduled RT
 - Effects stream
 - Software based volume/pan control
 - Accurate scope/audio syncing using ALSA features
 - Portable (well, we'll see about that :)
 - Open source(tm)

%description -l pl
AlsaPlayer to nowy rodzaj odtwarzacza PCM. Jest wielow±tkowy i próbuje
solidnie przeæwiczyæ sterowniki i bibliotekê ALSA. Jego cechy to:

Wej¶cie:
 - obs³uga MP2 i MP3
 - obs³uga Ogg Vorbis (w podpakiecie)
 - obs³uga WAV, 8 i 16-bitowych, mono, stereo, dowolna czêstotliwo¶æ
 - obs³uga CD Digital Audio
 - odtwarzanie plików podmapowanych przez audiofs (CDDA)
 - obs³uga MAD - MPEG Audio
 - obs³uga modu³ów (mikmod) (w podpakiecie)

Wyj¶cie:
 - OSS - natywne sterowniki z j±dra
 - ALSA - oczywi¶cie najlepiej obs³ugiwana :) (w podpakiecie)
 - Sparc - sterowniki d¼wiêku dla UltraSparca
 - SGI - biblioteka sterowników d¼wiêku SGI
 - ESD - obs³uga O¶wieconego demona d¼wiêku (w podpakiecie)
 - NAS - Sieciowego Systemu Audio (w podpakiecie)
 - null :-)

Wizualizacja:
 - Stereoskop
 - Monoskop
 - Wska¼nik poziomu d¼wiêku
 - inne, wkrótce wiêcej...

Ogólne cechy:
 - Kontrola szybko¶ci (w obie strony)
 - obs³uga kolejki (playlisty)
 - obs³uga wielu wska¼ników naraz
 - wielow±tkowo¶æ
 - interfejs graficzny bazuj±cy na gtk+
 - operacje bez GUI na potrzeby skryptów
 - architektura wtyczek
 - programowa kontrola g³o¶no¶ci i balansu
 - synchronizacja d¼wiêku i wska¼ników przy u¿yciu mo¿liwo¶ci ALSA

%package input-mikmod
Summary:	Alsaplayer plugin for playing mod files
Summary(pl):	Wtyczka do alsaplayera do odtwarzania plików mod
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description input-mikmod
Alsaplayer plugin for playing mod files.

%description input-mikmod -l pl
Wtyczka do alsaplayera do odtwarzania plików mod.

%package input-vorbis
Summary:	Alsaplayer plugin for playing ogg/vorbis files
Summary(pl):	Wtyczka do alsaplayera do odtwarzania plików ogg/vorbis
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description input-vorbis
Alsaplayer plugin for playing ogg/vorbis files.

%description input-vorbis -l pl
Wtyczka do alsaplayera do odtwarzania plików ogg/vorbis.

%package input-audiofile
Summary:	Alsaplayer plugin for playing wave audio formats
Summary(pl):	Wtyczka do alsaplayera do odtwarzania plików audio typu wave
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description input-audiofile
Alsaplayer plugin for playing wave audio formats (like AIFF, AIFC,
WAVE, ...).

%description input-audiofile -l pl
Wtyczka do alsaplayera do odtwarzania plików audio typa wave (AIFF,
AIFC, WAVE, ...)

%package input-mad
Summary:	Alsaplayer plugin for playing MP3 files using MAD
Summary(pl):	Wtyczka do alsaplayera do odtwarzania plików MP3 przy pomocy MAD
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description input-mad
Alsaplayer plugin for playing MP3 files using MAD.

%description input-mad -l pl
Wtyczka do alsaplayera do odtwarzania plików MP3 przy pomocy MAD.

%package output-alsa
# this plugin come in two versions, for alsa 0.5.x and 0.9.x
# but this libraraies provide different .so number, so the
# version built will work only with correct alsa-lib version,
# what we do want :-)

Summary:	Alsaplayer plugin for playing through alsa drivers
Summary(pl):	Wtyczka do alsaplayera do odtwarzania przez sterowniki alsa
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description output-alsa
Alsaplayer plugin for playing sound through alsa drivers.

%description output-alsa -l pl
Wtyczka do alsaplayera do odtwarzania d¼wiêku przez sterowniki alsa.

%package output-esound
Summary:	Alsaplayer plugin for playing through esound daemon
Summary(pl):	Wtyczka do alsaplayera do odtwarzania przez demona esound
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description output-esound
Alsaplayer plugin for playing sound through esound daemon.

%description output-esound -l pl
Wtyczka do alsaplayera do odtwarzania d¼wiêku przez demona esound.

%package output-nas
Summary:	Alsaplayer plugin for playing through NAS daemon
Summary(pl):	Wtyczka do alsaplayera do odtwarzania przez demona NAS
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description output-nas
Alsaplayer plugin for playing sound through NAS (network audio system)
daemon.

%description output-nas -l pl
Wtyczka do alsaplayera do odtwarzania d¼wiêku przez demona NAS
(network audio system).


#%package reader-curl
#Summary:	Alsaplayer plugin for reading files from network
#Summary(pl):	Wtyczka do alsaplayera do odczytu plików z sieci
#Group:		X11/Applications/Multimedia
#Requires:	%{name} = %{version}
#
#%description reader-curl
#Alsaplayer plugin for reading files from network.
#
#%description reader-curl -l pl
#Wtyczka do alsaplayera do odczytu plików z sieci.

%package scopes-gtk
Summary:	Alsaplayer plugin for visualization
Summary(pl):	Wtyczka do alsaplayera do wizualizacji
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description scopes-gtk
Alsaplayer plugin for visualization.

%description scopes-gtk -l pl
tyczka do alsaplayera do wizualizacji.

%package scopes-opengl
Summary:	Alsaplayer plugin for visualization using OpenGL
Summary(pl):	Wtyczka do alsaplayera do wizualizacji z u¿yciem OpenGL
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description scopes-opengl
Alsaplayer plugin for visualization using OpenGL.

%description scopes-opengl -l pl
Wtyczka do alsaplayera do wizualizacji z u¿yciem OpenGL.

%package interface-gtk
Summary:	GTK+ interface for Alsaplayer
Summary(pl):	Interfejs GTK+ alsaplayera
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description interface-gtk
GTK+ interface for Alsaplayer.

%description interface-gtk -l pl
Interfejs GTK+ alsaplayera.

%package lib
Summary:	Library for remote control Alsaplayer
Summary(pl):	Biblioteka do zdalnego staerowania alsaplayerem
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description lib
Library for remote control Alsaplayer.

%description lib -l pl
Biblioteka do zdalnego staerowania alsaplayerem.

%package devel
Summary:	Library for remote control Alsaplayer - development files
Summary(pl):	Biblioteka do zdalnego staerowania alsaplayerem - pliki nag³ówkowe
Group:		X11/Applications/Multimedia
Requires:	%{name}-lib = %{version}

%description devel
Library for remote control Alsaplayer - development files.

%description devel
Biblioteka do zdalnego staerowania alsaplayerem - pliki nag³ówkowe.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS=" -I/usr/X11R6/include"
LDFLAGS="%{rpmldflags} -L/usr/X11R6/lib"
export CPPFLAGS LDFLAGS
%configure \
	--enable-alsa \
	--enable-audiofile \
	--enable-esd \
	--enable-gtk \
	--enable-mikmod \
	--enable-nas \
	--enable-oggvorbis \
	--enable-opengl \
	--enable-oss \
%ifarch sparc
	--enable-sparc
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_bindir}/alsaplayer
%dir %{_pkglibdir}
%dir %{_pkglibdir}/input
%attr(755,root,root) %{_pkglibdir}/input/libcdda.so
%{_pkglibdir}/input/libcdda.la
%attr(755,root,root) %{_pkglibdir}/input/libwav.so
%{_pkglibdir}/input/libwav.la
%dir %{_pkglibdir}/output
%attr(755,root,root) %{_pkglibdir}/output/liboss_out.so
%{_pkglibdir}/output/liboss_out.la
%attr(755,root,root) %{_pkglibdir}/output/libnull_out.so
%{_pkglibdir}/output/libnull_out.la
%ifarch sparc
%attr(755,root,root) %{_pkglibdir}/output/libsparc_out.so
%{_pkglibdir}/output/libsparc_out.la
%endif
%dir %{_pkglibdir}/interface
%attr(755,root,root) %{_pkglibdir}/interface/libtext.so
%{_pkglibdir}/interface/libtext.la
%attr(755,root,root) %{_pkglibdir}/interface/libdaemon.so
%{_pkglibdir}/interface/libdaemon.la
%dir %{_pkglibdir}/scopes
%dir %{_pkglibdir}/reader
%{_pkglibdir}/reader/libfile.la
%attr(755,root,root) %{_pkglibdir}/reader/libfile.so
%{_pkglibdir}/reader/libhttp.la
%attr(755,root,root) %{_pkglibdir}/reader/libhttp.so
%{_mandir}/man*/*

%files interface-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/interface/libgtk.so
%{_pkglibdir}/interface/libgtk.la

%files scopes-gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes/libblurscope.so
%{_pkglibdir}/scopes/libblurscope.la
%attr(755,root,root) %{_pkglibdir}/scopes/liblevelmeter.so
%{_pkglibdir}/scopes/liblevelmeter.la
%attr(755,root,root) %{_pkglibdir}/scopes/liblogbarfft.so
%{_pkglibdir}/scopes/liblogbarfft.la
%attr(755,root,root) %{_pkglibdir}/scopes/libmonoscope.so
%{_pkglibdir}/scopes/libmonoscope.la
%attr(755,root,root) %{_pkglibdir}/scopes/libspacescope.so
%{_pkglibdir}/scopes/libspacescope.la
%attr(755,root,root) %{_pkglibdir}/scopes/libsynaescope.so
%{_pkglibdir}/scopes/libsynaescope.la

%files scopes-opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/scopes/liboglspectrum.so
%{_pkglibdir}/scopes/liboglspectrum.la

%files input-mikmod
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmod.so
%{_pkglibdir}/input/libmod.la

%files input-vorbis
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libvorbis_in.so
%{_pkglibdir}/input/libvorbis_in.la

%files input-audiofile
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libaf.so
%{_pkglibdir}/input/libaf.la

%files input-mad
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/input/libmad_in.so
%{_pkglibdir}/input/libmad_in.la

%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libalsa_out.so
%{_pkglibdir}/output/libalsa_out.la

%files output-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libesound_out.so
%{_pkglibdir}/output/libesound_out.la

%files output-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libnas_out.so
%{_pkglibdir}/output/libnas_out.la

#%files reader-curl
#%defattr(644,root,root,755)
#%{_pkglibdir}/reader/libcurl.la
#%attr(755,root,root) %{_pkglibdir}/reader/libcurl.so

%files lib
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libalsaplayer.so.0.0.2

%files devel
%defattr(644,root,root,755)
%{_includedir}/alsaplayer
%{_libdir}/libalsaplayer.la
%{_libdir}/libalsaplayer.so
%{_pkgconfigdir}/alsaplayer.pc
