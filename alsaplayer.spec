Summary:	Alsaplayer - MP2/MP3/WAV/CD player
Summary(pl):	Alsaplayer - odtwarzacz MP2/MP3/WAV/CD
Name:		alsaplayer
Version:	0.99.60
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	ftp://ftp.alsa-project.org/pub/people/andy/%{name}-%{version}.tar.bz2
Patch0:		%{name}-nas.patch
Patch1:		%{name}-docs.patch
BuildRequires:	alsa-lib-devel
BuildRequires:	audiofile-devel
BuildRequires:	esound-devel
BuildRequires:	gtk+-devel
BuildRequires:	libmikmod-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	nas-devel
BuildRequires:	libtool
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package output-alsa
# this plugin come in two versions, for alsa 0.5.x and 0.9.x
# but this libraraies provide different .so number, so the
# version built will work only with correct alsa-lib version,
# what we do want :-)

Summary:	Alsaplayer plugin for playing through alsa drivers
Summary(pl):	Wtyczka do alsaplayera do odtwarzania przez drivery alsa
Group:		X11/Applications/Multimedia
Requires:	%{name} = %{version}

%description output-alsa
Alsaplayer plugin for playing sound through alsa drivers.

%description output-alsa -l pl 
Wtyczka do alsaplayera do odtwarzania d¼wiêku przez drivery alsa.

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
Alsaplayer plugin for playing sound through NAS (network audio
system) daemon.

%description output-nas -l pl 
Wtyczka do alsaplayera do odtwarzania d¼wiêku przez demona NAS
(network audio system).

%define		_pkglibdir	%{_libdir}/%{name}
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
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

gzip -9nf AUTHORS README ChangeLog

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/alsaplayer
%dir %{_pkglibdir}
%dir %{_pkglibdir}/input
%attr(755,root,root) %{_pkglibdir}/input/libcdda.so
%{_pkglibdir}/input/libcdda.la
%attr(755,root,root) %{_pkglibdir}/input/libwav.so
%{_pkglibdir}/input/libwav.la
%attr(755,root,root) %{_pkglibdir}/input/libmad_in.so
%{_pkglibdir}/input/libmad_in.la
%dir %{_pkglibdir}/output
%attr(755,root,root) %{_pkglibdir}/output/liboss.so
%{_pkglibdir}/output/liboss.la
%attr(755,root,root) %{_pkglibdir}/output/libnull.so
%{_pkglibdir}/output/libnull.la
%ifarch sparc
%attr(755,root,root) %{_pkglibdir}/output/libsparc.so
%{_pkglibdir}/output/libsparc.la
%endif
%attr(755,root,root) %{_pkglibdir}/interface/lib*.so
%{_pkglibdir}/interface/lib*.la
%attr(755,root,root) %{_pkglibdir}/scopes/lib*.so
%{_pkglibdir}/scopes/lib*.la
%{_mandir}/man*/*

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

%files output-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libalsa.so
%{_pkglibdir}/output/libalsa.la

%files output-esound
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libesound.so
%{_pkglibdir}/output/libesound.la

%files output-nas
%defattr(644,root,root,755)
%attr(755,root,root) %{_pkglibdir}/output/libnas.so
%{_pkglibdir}/output/libnas.la
