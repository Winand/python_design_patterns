import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import NamedTuple, Protocol


class VideoExporter(Protocol):
    "Basic representation of video exporting codec."

    def prepare_export(self, video_data: bytes) -> None:
        "Prepare video data for exporting."

    def do_export(self, folder: Path) -> None:
        "Export the video data to a folder."


class LosslessVideoExporter:
    "Lossless video exporting codec."

    def prepare_export(self, video_data: bytes) -> None:  # noqa: ARG002
        "Prepare video data for exporting."
        print("Preparing video data for lossless export.")

    def do_export(self, folder: Path) -> None:
        "Export the video data to a folder."
        print(f"Exporting video data in lossless format to '{folder}'.")


class H264BPVideoExporter:
    "H.264 video exporting codec with Baseline profile."

    def prepare_export(self, video_data: bytes) -> None:  # noqa: ARG002
        "Prepare video data for exporting."
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: Path) -> None:
        "Export the video data to a folder."
        print(f"Exporting video data in H.264 (Baseline) format to '{folder}'.")


class H264Hi422PVideoExporter:
    "H.264 video exporting codec with Hi422P profile (10-bit, 4:2:2 chroma sampling)."

    def prepare_export(self, video_data: bytes) -> None:  # noqa: ARG002
        "Prepare video data for exporting."
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: Path) -> None:
        "Export the video data to a folder."
        print(f"Exporting video data in H.264 (Hi422P) format to '{folder}'.")


class AudioExporter(Protocol):
    "Basic representation of audio exporting codec."

    def prepare_export(self, audio_data: bytes) -> None:
        "Prepare audio data for exporting."

    def do_export(self, folder: Path) -> None:
        "Export the audio data to a folder."


class AACAudioExporter:
    "AAC audio exporting codec."

    def prepare_export(self, audio_data: bytes) -> None:  # noqa: ARG002
        "Prepare audio data for exporting."
        print("Preparing audio data for AAC export.")

    def do_export(self, folder: Path) -> None:
        "Export the audio data to a folder."
        print(f"Exporting audio data in AAC format to '{folder}'.")


class WAVAudioExporter:
    "WAV (lossless) audio exporting codec."

    def prepare_export(self, audio_data: bytes) -> None:  # noqa: ARG002
        "Prepare audio data for exporting."
        print("Preparing audio data for WAV export.")

    def do_export(self, folder: Path) -> None:
        "Export the audio data to a folder."
        print(f"Exporting audio data in WAV format to '{folder}'.")


@dataclass
class MediaExporter:
    "A dataclass that represents a combination of concrete video and audio codecs."

    video: VideoExporter
    audio: AudioExporter


@dataclass
class MediaExporterFactory:
    "A dataclass that represents a combination of video and audio export classes."

    video_class: type[VideoExporter]
    audio_class: type[AudioExporter]

    def __call__(self) -> MediaExporter:
        "Instantiate video and audio exporters."
        return MediaExporter(self.video_class(), self.audio_class())


def parse_arguments() -> argparse.Namespace:
    "Parse command line arguments."
    # read the desired export quality
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--quality",
        "-q",
        choices=["low", "high", "master"],
        required=True,
    )
    return parser.parse_args()


def to_exporter(export_quality: str) -> MediaExporterFactory:
    """
    Return video and audio exporters based on the given quality as a string.

    This is implemented as a Simple Factory coding idiom.
    """
    # WARN: instead of a separate Abstract Factory all exporter combinations
    # are defined in this Simple Factory which leads to a little lower cohesion
    factories = {
        # High speed, lower quality audio and video export
        "low": MediaExporterFactory(H264BPVideoExporter, AACAudioExporter),
        # Slower speed, high quality audio and video export
        "high": MediaExporterFactory(H264Hi422PVideoExporter, AACAudioExporter),
        # Low speed, master quality audio and video export
        "master": MediaExporterFactory(LosslessVideoExporter, WAVAudioExporter),
    }
    if export_quality in factories:
        return factories[export_quality]
    msg = f"Unknown output quality option: {export_quality}"
    raise ValueError(msg)


def main(exporter: MediaExporter) -> None:
    "Try out the Abstract Factory pattern."
    print("Hello from factory!")

    # prepare the export
    exporter.video.prepare_export(b"placeholder_for_video_data")
    exporter.audio.prepare_export(b"placeholder_for_audio_data")

    # do the export
    folder = Path("./export")
    exporter.video.do_export(folder)
    exporter.audio.do_export(folder)


if __name__ == "__main__":
    args = parse_arguments()
    factory = to_exporter(args.quality)
    media_exporter = factory()
    main(media_exporter)
