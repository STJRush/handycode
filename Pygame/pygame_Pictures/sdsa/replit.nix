{ pkgs }: {
	deps = [
   pkgs.portmidi
   pkgs.pkg-config
   pkgs.libpng
   pkgs.libjpeg
   pkgs.freetype
   pkgs.fontconfig
   pkgs.SDL2_ttf
   pkgs.SDL2_mixer
   pkgs.SDL2_image
   pkgs.SDL2
		pkgs.python38Full
	];
  env = {
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath ([
      # Neded for pandas / numpy
      pkgs.stdenv.cc.cc.lib
      pkgs.zlib
      # Needed for pygame
      pkgs.glib
    ] ++ (with pkgs.xlibs; [ libX11 libXext libXinerama libXcursor libXrandr libXi libXxf86vm ]));

    PYTHONBIN = "${pkgs.python38Full}/bin/python3.8";
  };
}