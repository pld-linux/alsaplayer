Summary: Alsaplayer
Name: alsaplayer
Version: 0.99
Release: 21
Copyright: Opensource
Group: Applications/Multimedia
Source: http://www.alsa-project.org/~andy/alsaplayer-%{version}.%{release}.tar.gz
Requires:  glib-1.2.1 gtk+-1.2.1
BuildRoot: /var/tmp/%{name}-%{version}-%{release}.root

%description
AlsaPlayer is a new type of PCM player. It is heavily multi-threaded and
tries to excercise the ALSA library and driver quite a bit. Features
include: 

Input addons:

     MP2 and MP3 support 
     WAV support, 8-, 16-bit, mono, stereo, any sample rate 
     CDDA support, CD Digital Audio playback! and thus USB ready :) 
     Also plays files mapped by audiofs (CDDA) 
     Module support in progress... 

Output addons:

     ALSA. Best supported of course :) 
     OSS. Kernel native sound drivers 
     Sparc. UltraSparc sound drivers 
     SGI. SGI audio library driver 
     ESD. Enlightened sound daemon support 

Visual scopes:

     Stereoscope 
     Monoscope 
     Levelmeter 
     Spacescope 
     FFTscope 
     FFTscope II 
     More being developed... 

General features:

     Full speed (pitch) control, positive *and* negative! 
       (First Linux player that does this!! MP3's and CD's do varispeed :) 
     Queue (playlist) support 
     Concurrent visual scopes (open as many as you want) 
     Multi-threaded design for efficient/skip free playback (RT) 
     GUI Interface based on gtk+ 
     NOGUI operation for shell script usage 
     Plug-in core architecture 
     Low latency mode, as low as 5ms when scheduled RT 
     Effects stream 
     Software based volume/pan control 
     Accurate scope/audio syncing using ALSA features 
     Portable (well, we'll see about that :) 
     Open source(tm) 
     Y2K complient (doh!)

RPM built by Miles Lott<milos@insync.net> 7/1/1999
%prep

%setup -n alsaplayer-%{version}.%{release}
CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=/usr

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/doc/alsaplayer-%{version}-%{release}
make DESTDIR=$RPM_BUILD_ROOT install
cp AUTHORS COPYING INSTALL README README.ESD README.OSS $RPM_BUILD_ROOT/usr/doc/alsaplayer-%{version}-%{release}

%clean
rm -rf $RPM_BUILD_ROOT

%doc AUTHORS COPYING INSTALL README README.ESD README.OSS

%files
%defattr(-,root,root)
/usr/bin/alsaplayer
/usr/doc/alsaplayer-%{version}-%{release}/AUTHORS
/usr/doc/alsaplayer-%{version}-%{release}/COPYING
/usr/doc/alsaplayer-%{version}-%{release}/INSTALL
/usr/doc/alsaplayer-%{version}-%{release}/README
/usr/doc/alsaplayer-%{version}-%{release}/README.ESD
/usr/doc/alsaplayer-%{version}-%{release}/README.OSS
/usr/lib/alsaplayer/output/libalsa.a
/usr/lib/alsaplayer/output/libalsa.la
/usr/lib/alsaplayer/output/libalsa.so
/usr/lib/alsaplayer/output/libesound.a
/usr/lib/alsaplayer/output/libesound.la
/usr/lib/alsaplayer/output/libesound.so
/usr/lib/alsaplayer/output/liboss.a
/usr/lib/alsaplayer/output/liboss.la
/usr/lib/alsaplayer/output/liboss.so
/usr/lib/alsaplayer/input/libaplay.a
/usr/lib/alsaplayer/input/libaplay.la
/usr/lib/alsaplayer/input/libaplay.so
/usr/lib/alsaplayer/input/libcdda.a
/usr/lib/alsaplayer/input/libcdda.la
/usr/lib/alsaplayer/input/libcdda.so
/usr/lib/alsaplayer/input/libmpg123.a
/usr/lib/alsaplayer/input/libmpg123.la
/usr/lib/alsaplayer/input/libmpg123.so
